from astropy import units as u
import numpy as np


class UnitConstants:
    ERG_S_CM2_HZ = (u.erg / u.cm ** 2 / u.s / u.Hz)
    ABMAG = "abmag"
    STMAG = "stmag"
    STZERO = -21.10  # ST mag zero point
    ABZERO = -48.60  # AB mag zero point


def flux_density2mag(flux, flux_err, spec, spec_unit,
                     flux_unit=UnitConstants.ERG_S_CM2_HZ,
                     mag_unit=UnitConstants.ABMAG):
    """
    Convert a flux density value or array to magnitude units (AB or ST)
    :param flux: (float or array-like of floats) flux value(s) to convert
    :param flux_err: (float or array-like of floats) flux error(s) to convert
    :param spec: (float or array-like of floats) respective spectral value(s)
    :param spec_unit: (astropy.unit) spectral unit
    :param flux_unit: (astropy.unit) original flux unit
    :param mag_unit: (astropy.unit) magnitude unit ("abmag" or "stmag") to
    convert to
    :return: a tuple of the converted flux +/- flux_err,
    in mag_units
    """

    # convert flux units to erg/s/cm2/Hz
    if flux_unit != UnitConstants.ERG_S_CM2_HZ:
        flux = flux2ergs_cm2_s_hz(flux, flux_unit, spec, spec_unit)
        flux_err = flux2ergs_cm2_s_hz(flux_err, flux_unit, spec, spec_unit)

    m = 0;  # magnitude

    if mag_unit == UnitConstants.ABMAG:
        m = -2.5 * np.log10(flux) + UnitConstants.ABZERO
    elif mag_unit == UnitConstants.STMAG:
        m = -2.5 * np.log10(flux) + UnitConstants.STZERO
    else:
        raise ValueError("Unrecognized magnitude unit used.")

    m_err = -2.5 * np.log10(1 + flux_err / flux)  # magnitude uncertainty

    return m, m_err


def flux2ergs_cm2_s_hz(flux, flux_unit, spec, spec_unit):
    """
    Convert fluxes to erg/s/cm2/Hz
    :param flux: (float or array-like of floats) flux value(s) to convert
    :param flux_unit: (astropy.unit) flux unit
    :param spec: (float or array-like of floats) respective spectral value(s)
    :param spec_unit: (astropy.unit) spectral unit
    :return: flux values converted to erg/s/cm2/Hz
    """

    flux = flux * flux_unit.to(UnitConstants.ERG_S_CM2_HZ,
                               equivalencies=u.spectral_density(
                                   spec * spec_unit))

    return flux


def ergs_cm2_s_hz2flux(flux, flux_unit, spec, spec_unit):
    """
    Convert fluxes from erg/s/cm2/Hz to flux_unit
    :param flux: (float or array-like of floats) flux value(s) to convert
    :param flux_unit: (astropy.unit) flux unit
    :param spec: (float or array-like of floats) respective spectral value(s)
    :param spec_unit: (astropy.unit) spectral unit
    :return: flux values converted to erg/s/cm2/Hz
    """

    flux = flux * UnitConstants.ERG_S_CM2_HZ\
        .to(flux_unit, equivalencies=u.spectral_density(spec * spec_unit))

    return flux


def flux2flux(flux, from_flux_unit, to_flux_unit, spec, from_spec_unit,
              to_spec_unit=None):
    """
    Convert between two flux density units and spectral units
    :param flux: (float or array-like of floats) flux value(s) to convert
    :param from_flux_unit: (astropy.unit) flux unit to convert from
    :param to_flux_unit: (astropy.unit) flux unit to convert to
    :param spec: (float or array-like of floats) respective spectral value(s)
    :param from_spec_unit: (astropy.unit) spectral unit to convert from
    :param to_spec_unit: (astropy.unit) spectral unit to convert to
    :return: a tuple of the flux and spectral values converted to to_flux_unit
    and to_spec_unit
    """

    if to_spec_unit is None:
        to_spec_unit = from_spec_unit

    new_spec = spec * from_spec_unit.to(to_spec_unit)

    flux = flux * from_flux_unit.to(to_spec_unit,
                                    equivalencies=u.spectral_density(new_spec * from_spec_unit))

    return flux, new_spec


def mag2flux_density(mag, mag_unit, spec, spec_unit,
                     flux_unit=UnitConstants.ERG_S_CM2_HZ, mag_err=None):
    """
    Convert from a magnitude (AB or ST) to any flux density unit.
    :param mag: (float or array-like of floats) magnitude(s) to convert
    :param mag_err: (float or array-like of floats) magnitude error(s) to
    convert
    :param mag_unit: (astropy.unit) magnitude unit ("abmag" or "stmag")
    :param flux_unit: (astropy.unit) flux unit to convert to
    :return: a tuple of the converted magnitude +/- magnitude errors,
    in flux_units
    """

    # magnitude to erg/s/cm2/Hz convertion
    if mag_unit == UnitConstants.ABMAG:
        flux = 10 ** (-0.4(mag - UnitConstants.ABZERO))
        flux_err = 10 ** (-0.4(mag + mag_err - UnitConstants.ABZERO)) - flux
    elif mag_unit == UnitConstants.STMAG:
        flux = 10 ** (-0.4(mag - UnitConstants.STZERO))
        flux_err = 10 ** (-0.4(mag + mag_err - UnitConstants.STZERO)) - flux
    else:
        raise ValueError("Unrecognized magnitude unit used.")

    # convert the units to flux_units
    if flux_unit != UnitConstants.ERG_S_CM2_HZ:
        flux = ergs_cm2_s_hz2flux(flux, flux_unit, spec, spec_unit)
        flux_err = ergs_cm2_s_hz2flux(flux_err, flux_unit, spec, spec_unit)

    return flux, flux_err

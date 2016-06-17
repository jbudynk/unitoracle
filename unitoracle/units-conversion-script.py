from unitoracle import *

# a script to investigate how to do basic units conversions.
# change it to you heart's content :)

# easy case: erg/s/cm2/Hz to ABMAG
x = np.arange(5)+1
y = x
err = y*0.1

y_unit = u.erg / u.cm**2 / u.second / u.Hz
x_unit = u.Hz

print "Original values in " + str(y_unit) + " vs "+ str(x_unit) + ": "
for i in range(0, x.size):
    print str(x[i]) + " +/- (" + str(err[i]) + ")"

print "Converted to ABMAG: "
abmag, abmag_err = flux_density2mag(y, err, x, x_unit)
for i in range(0, abmag.size):
    print str(abmag[i]) + " +/- (" + str(abmag_err[i]) + ")"

print "Converted back to "+ str(y_unit) + ": "
new_flux, new_flux_err = mag2flux_density(abmag, abmag_err, x, x_unit)
for i in range(0, abmag.size):
    print str(new_flux[i]) + " +/- (" + str(new_flux_err[i]) + ")"

print ''
print ''

# other cases

x_unit = u.AA
y_unit = u.erg / u.cm**2 / u.second / u.AA

x = np.arange(10)+5000
y = np.arange(10)*10+1
err = np.ones(x.size) * 0.1

print "Original values in " + str(y_unit) + " vs "+ str(x_unit) + ": "
for i in range(0, x.size):
    print str(y[i]) + " +/- (" + str(err[i]) + ")"

abmag, abmag_err = flux_density2mag(y, err, x, x_unit,
                                    flux_unit=y_unit,
                                    mag_unit=UnitConstants.ABMAG)

print "Converted to ABMAG: "
for i in range(0, abmag.size):
    print str(abmag[i]) + " +/- (" + str(abmag_err[i]) + ")"

new_flux, new_flux_err = mag2flux_density(abmag, abmag_err, x, x_unit,
                                          flux_unit=y_unit,
                                          mag_unit=UnitConstants.ABMAG)

print "Converted back to "+ str(y_unit) + ": "
for i in range(0, abmag.size):
    print str(new_flux[i]) + " +/- (" + str(new_flux_err[i]) + ")"

# convert between any units
print ""
print ""
print "Convert between any other flux units with flux2flux(): "
print ""

print "Original values in " + str(y_unit) + " vs "+ str(x_unit) + ": "
for i in range(0, x.size):
    print str(y[i]) + " +/- (" + str(err[i]) + ")"

y1 = y
y1err = err
y1_unit = y_unit
x1 = x
x1_unit = x_unit

y2_unit = u.W / u.cm**2 / u.um

print "Converted from erg/s/cm2/A vs A to Watt/cm2/um vs Hz: "
y2, x2 = flux2flux(y1, y1_unit, y2_unit, x1, x1_unit, to_spec_unit=u.Hz)
y2err, tmp = flux2flux(y1err, y1_unit, y2_unit, x1, x1_unit, to_spec_unit=u.Hz)

for i in range(0, abmag.size):
    print str(y2[i]) + " +/- (" + str(y2err[i]) + ")"

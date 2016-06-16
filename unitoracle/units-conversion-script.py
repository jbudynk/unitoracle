import numpy as np
import astropy.units as u

from unitoracle import flux2ergs_cm2_s_hz

# a script to investigate how to do basic units conversions.

# let's start simple.
x = np.arange(10)+1
y = np.ones(10)+1
err = np.ones(x.size) * 0.1

# say these are in Jy, and we want to convert to AB magnitudes.
ABZERO = -48.60  # AB magnitude zero point

m_ab = -2.5 * np.log10(y) + ABZERO
m_ab_err = -2.5 * np.log10(1 + err/y)




x = 5000.
y = 10.
err = 1.

x_unit = u.AA
y_unit = u.erg / u.cm**2 / u.second / u.AA

print flux2ergs_cm2_s_hz(y, y_unit, x, x_unit)


x = np.arange(10)+5000
y = np.ones(10)*10
err = np.ones(x.size) * 0.1

print flux2ergs_cm2_s_hz(y, y_unit, x, x_unit)





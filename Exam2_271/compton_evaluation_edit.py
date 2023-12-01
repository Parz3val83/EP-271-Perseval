#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This Python 3 module contains a function for evaluating the
# Compton scattering effect.

def compton(wavein,theta,hcon=6.626e-34,clight=2.998e8,emass=9.109e-31):
    """
    This function evaluates how a photon is changed when it
    scatters off an electron.
    
    Parameters
    ----------
    wavein : floating-point number
        photon wave property before the collision.
    theta : floating-point number
        scattering angle in radians.
    hcon : floating-point number, optional
        Planck's constant. The default is 6.626e-34 for SI units.
    clight : floating-point number, optional
        speed of light. The default is 2.998e8 for m/s.
    emass : floating-point number, optional
        electron mass. The default is 9.109e-31 for kg.

    Returns
    -------
    waveout : floating-point number
        photon wave property after the collision.
    """
    import math          #COMPLETE THIS LINE
    waveout= wavein/(1+hcon*wavein/(emass*clight**2)*1-math.cos(theta))       #COMPLETE THIS LINE
    return waveout

# Main program

# ADD PROGRAMMING THAT USES YOUR COMPLETED COMPTON FUNCTION
# FOR THE GIVEN ANGLE AND WAVE PROPERTY.

# ALSO, PRINT THE DESIRED RESULT.

val1=compton(1.5e19,1.047195751)

ratio=1.5e19/val1

print(val1)


print(ratio)

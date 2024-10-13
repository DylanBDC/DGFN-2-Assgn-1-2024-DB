'''
TPRG 2131 Fall 202x Assignment 1, Test file template.
Sept, 202x
Phil J <philip.jarvis@durhamcollege>


This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''


# Dylan Brett (100933134)
# TPRG-2131-02
# Oct 13, 2024
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s). I havent used any
# code from other sources other than referncing the course material.


# the video i used to figure out how pytest works: https://www.youtube.com/watch?v=P568DYHSPss

import pytest # imports the pytest module
from A_V_calc_DBv9 import circle_area, rectangle_area, cylinder_volume, triangle_area, sphere_volume # imports the different functions from A_V_calc_DBv9


def test_circle_area(): # this function tests the function circle_area in the main program
    assert circle_area('d', 5) == 78.5 # passes the mode and radius and checks to see if the rounded calculation is the same
    assert circle_area('v', 10) == 314.2 # passes the ,ode v and checks a different radius value


#def rectangle_area():



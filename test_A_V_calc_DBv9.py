
#def rectangle_area():
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
    assert circle_area('d', 2.2) == 15.2

def test_rectangle_area():
    assert rectangle_area('d', 5, 10) == 50
    assert rectangle_area('v', 7, 10) == 70
    assert rectangle_area('d', 1.1, 2.3) == 2.5



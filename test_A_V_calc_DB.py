
# Dylan Brett (100933134)
# TPRG-2131-02
# Oct 14, 2024
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s). I havent used any
# code from other sources other than referncing the course material.

# the video i used to figure out how pytest works: https://www.youtube.com/watch?v=P568DYHSPss


import pytest # imports the pytest module
from A_V_calc_DB import circle_area, rectangle_area, cylinder_volume, triangle_area, sphere_volume # imports the different functions from A_V_calc_DBv9


def test_circle_area(): # this function tests the function circle_area in the main program
    assert circle_area('d', 5) == 78.5 # passes the mode and radius and checks to see if the rounded calculation is the same
    assert circle_area('v', 10) == 314.2 # passes the mode v and checks a different radius value
    assert circle_area('d', 2.2) == 15.2 # checking the calculations with a float

def test_rectangle_area(): # tests the function rectangle_area
    assert rectangle_area('d', 5, 10) == 50 # passing the length and width of the rectangle to be calculated
    assert rectangle_area('v', 7, 10) == 70
    assert rectangle_area('d', 1.1, 2.3) == 2.5  # checking the calculations with a float

def test_cylinder_volume(): # tests the function cylinder_volume
    assert cylinder_volume('d', 5, 10) == 785.4 # passing the radius and height to be calculated
    assert cylinder_volume('v', 7, 10) == 1539.4
    assert cylinder_volume('d', 1.1, 2.3) == 8.7  # checking the calculations with a float
    
def test_triangle_area(): # tests the function triangle_area
    assert triangle_area('d', 5, 10) == 25 # passing the base and base height of the triangle to be calculated
    assert triangle_area('v', 7, 10) == 35
    assert triangle_area('d', 1.1, 2.3) == 1.3  # checking the calculations with a float
    
def test_sphere_volume(): # tests the function sphere_volume
    assert sphere_volume('d', 5) == 523.6 # passing the radius to the main program to be calculated
    assert sphere_volume('v', 7) == 1436.8 
    assert sphere_volume('d', 2.3) == 51  # checking the calculations with a float



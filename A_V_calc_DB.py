'''
TPRG 2131 Fall 202* Assignment 1
Sept, 202*
Phil J <philip.jarvis@durhamcollege>

Use this template as the start

*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''

# Dylan Brett (100933134)
# TPRG-2131-02
# Oct 10, 2024
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s). I havent used any
# code from other sources other than referncing the course material.

import math

# for the v/V and d/D part i would like to try and use classes to select which option to display (try and create a class for each calc function to pick calculated view or default)

class Mode: # this class handles switching between the calculated and default views
    def __init__(self):
        self.mode = 'd' # start off setting the mode to the default view
    
    def selected_mode(self, mode): #this function determines if v or d was selected (try adding try and except later)(not working yet)
        
        if (mode == 'v'):
            self.mode='v'
        else:
            self.mode='d'
        return self.mode
        

class Circle_a:
    
    def __init__(self, mode):
        self.mode = mode  # Mode is passed when creating the Circle object

    def circle_area(self): # this function calculates the area of a circle
        radius=input("what is the radius? ")
        area= math.pi * radius**2 # calculation came from my brain
        
        if self.mode.selected_mode(self.mode.mode) == 'v':
            print('equation')
            #return "display the full equation"  # Display formula and result
        else:
            print('default view')
            #return area  # Only display result
        

    
class Rectangle():

    def rectangle_area():
        print("rectangle calc")

class Cylinder():

    def cylinder_volume():
        print("cylinder calc")

class Triangle():

    def triangle_area():
        print("triangle calc")

class Circle_v():

    def circle_volume():
        print("circle volume calc")



mode=Mode()
while True:
    print('''
    A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	(Level 1)
    1.	Area of a circle calulation
    2.	Area of a rectangle calculation
    3.	Volume of a cylinder calculation
    4.	Area of a triangle calculation
    5.	Fifth Area/Volume* calculation''')
    
    
    level_0_1 = input("level 0 and 1 input section: ")
    
    if (level_0_1.lower()=='q'):
        exit('thanks for using this calculator')
        
    elif (level_0_1.lower()=='v'):
        #mode=Mode()
        mode.selected_mode('v')
        print('\nEquation View')
        
    
    elif (level_0_1.lower()=='d'):
        #mode=Mode()
        mode.selected_mode('d') 
        print('\nDefault View')
        
    elif (level_0_1=='1'):
        #mode=Mode()
        circle = Circle_a(mode)
        circle.circle_area()
        print('1')
    
    elif (level_0_1=='2'):
        print('2')
        
    elif (level_0_1=='3'):
        print('3')
        
    elif (level_0_1=='4'):
        print('4')
        
    elif (level_0_1=='5'):
        print('5')
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    
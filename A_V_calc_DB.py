
# Dylan Brett (100933134)
# TPRG-2131-02
# Oct 14, 2024
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s). I havent used any
# code from other sources other than referncing the course material (other than what i have put below). 

#cited
#triangle area calc  (https://www.google.com/search?q=area+of+a+triangle&rlz)
#sphere volume calac (https://www.google.com/search?q=sphere+volume&rlz)
#the video i used to figure out how pytest works: (https://www.youtube.com/watch?v=P568DYHSPss)
#cylinder volume calc (https://www.google.com/search?q=cylinder+volume&sca_esv)

import math
  
def selected_mode(mode): #this function determines if v or d was selected (try adding try and except later)
    if (mode == 'v'):# will make sure mode is set to either v or d 
        mode='v'
    else:
        mode='d'
    return mode # returns the value of mode to the selected_mode function


def circle_area(mode, radius): # this function calculates the area of a circle and rounds it, after rounding the result it will print the desired output (depending on the mode)
    area= (math.pi) * (radius**2) # calculation came from my brain/google
    area_rounded= round(area, 1) # rounds the result to one decimal place   
    
    if mode == 'v':
        print(f'\nequation result: \u03C0 * {radius}\u00B2 = {area_rounded}  (\u03C0 * r\u00B2 = area)')# Display formula and result (I havent added m^2 to the answer because the user could enter another unit as the input so the proper units could be cm^2 etc)
    else:
        print(f'\ndefault result: \u03C0 * {radius}\u00B2 = {area_rounded}')# Only display result
    return area_rounded # return the value to the function to be tested in pytest
         
        
def rectangle_area(mode, length, width): # this function calculates the area of a rectangle and rounds it, after rounding the result it will print the desired output (depending on the mode)
    area= (length) * (width) # calculation came from my brain/google
    area_rounded= round(area, 1) # rounds the result to one decimal place   
    
    if mode == 'v':
        print(f'\nequation result: {length} * {width} = {area_rounded}  (length * width = area)')# Display formula and result
    else:
        print(f'\ndefault result: {length} * {width} = {area_rounded}')# Only display result
    return area_rounded # return the value to the function to be tested in pytest


def cylinder_volume(mode, radius, height): # this function calculates the volume of a cylinder and rounds it, after rounding the result it will print the desired output (depending on the mode)
    volume= (math.pi) * (radius**2) * (height) # calculation came from my brain/google
    volume_rounded= round(volume, 1) # rounds the result to one decimal place   
    
    if mode == 'v':
        print(f'\nequation result: \u03C0 * {radius}\u00B2 * {height} = {volume_rounded}  (\u03C0 * radius\u00B2 * height = volume)')# Display formula and result
    else:
        print(f'\ndefault result: \u03C0 * {radius}\u00B2 * {height} = {volume_rounded}')# Only display result
    return volume_rounded # return the value to the function to be tested in pytest


def triangle_area(mode, base, base_height): # this function calculates the area of a triangle and rounds it, after rounding the result it will print the desired output (depending on the mode)
    area= (0.5) * (base) * (base_height) # calculation came from google
    area_rounded= round(area, 1) # rounds the result to one decimal place   
    
    if mode == 'v':
        print(f'\nequation result: 0.5 * ({base} * {base_height}) = {area_rounded}  ( 0.5 * (base * base_height) = area )')# Display formula and result
    else:
        print(f'\ndefault result: 0.5 * ({base} * {base_height}) = {area_rounded}')# Only display result
    return area_rounded # return the value to the function to be tested in pytest


def sphere_volume(mode, radius): # this function calculates the volume of a sphere and rounds it, after rounding the result it will print the desired output (depending on the mode)
    volume= (4/3) * ((math.pi) * (radius**3)) # calculation came from google
    volume_rounded= round(volume, 1) # rounds the result to one decimal place   
    
    if mode == 'v':
        print(f'\nequation result: 4/3 * (\u03C0 * {radius}\u00B3) = {volume_rounded}  ( 4/3 * (\u03C0 * radius) = volume )')# Display formula and result
    else:
        print(f'\ndefault result: 4/3 * (\u03C0 * {radius}\u00B3) = {volume_rounded}')# Only display result
    return volume_rounded # return the value to the function to be tested in pytest


def main(): # mainguard (blocks pytest from running this function)
    
    mode = 'd' # start off the display in the default view (outside of the loop so it doesnt reset to d every time)(in mainguard so not a global variable)
    
    #level 0 message
    print('A/V calculator\n')
    print('Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.\nEnter V/v to change the calculated view or D/d for default view.')
    
    while True: # main loop of the program
        # level 1 message inside the while loop
        print('''
    1.	Area of a circle calulation
    2.	Area of a rectangle calculation
    3.	Volume of a cylinder calculation
    4.	Area of a triangle calculation
    5.	Volume of a sphere calculation''')
    
    
        level_0_1 = input("Please provide an input: ") # one input for both menus
    
        if (level_0_1.lower()=='q'):
            exit('thanks for using this calculator') # when q is entered the program exits with an exit message
        
        elif (level_0_1.lower()=='v'):
            mode = selected_mode('v') # sends v to the function selected_mode and sets the mode
            print('\nEquation View') # message showing the current view
    
        elif (level_0_1.lower()=='d'):
            mode = selected_mode('d') # sends d to the function selected_mode and sets the mode
            print('\nDefault View') # message showing the current view
        
        elif (level_0_1=='1'):
            radius=float(input("what is the radius? ")) # either a float (1.1) or an integer (1.0) can be entered (can add a decimal if they want)
            circle_area(mode, radius) # calls the function with the arguments mode and radius
    
        elif (level_0_1=='2'):
            length=float(input("what is the length of the rectangle? "))
            width=float(input("what is the width of the rectangle? "))
            rectangle_area(mode, length, width) # calls the function with the arguments mode, length, and width
        
        elif (level_0_1=='3'):
            radius=float(input("what is the radius of the cylinder? "))
            height=float(input("what is the height of the cylinder? "))
            cylinder_volume(mode, radius, height) # calls the function with the arguments mode, radius, and height
        
        elif (level_0_1=='4'):
            base=float(input("what is the length of the base of the triangle? "))
            base_height=float(input("what is the height of the base of the triangle? "))
            triangle_area(mode, base, base_height) # calls the function with the arguments mode, base, and base_height
        
        elif (level_0_1=='5'):
            radius=float(input("what is the radius of the sphere? "))
            sphere_volume(mode, radius) # calls the function with the arguments mode, radius

if __name__ == "__main__": # mainguard (blocks pytest from running this function)(but runs the function if in correct file)
    main()
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    

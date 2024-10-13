# Dylan Brett (100933134)
# TPRG-2131-02
# Oct 12, 2024
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s). I havent used any
# code from other sources other than referncing the course material.

import math

   
def selected_mode(mode): #this function determines if v or d was selected (try adding try and except later)
      
    if (mode == 'v'):#
        mode='v'
    else:
        mode='d'
    return mode # returns the value of mode to the selected_mode function

def circle_area(mode): # this function calculates the area of a circle
    radius=float(input("what is the radius? "))
    #radius_float=float(radius)
    area= math.pi * radius**2 # calculation came from my brain
    area_rounded= round(area, 1) # rounds the result to one decimal place   
    if mode == 'v':
        print(f'equation result: \u03C0 * {radius}^2 = {area_rounded}m^2  (\u03C0 * r^2 = area)')# Display formula and result
        
    else:
        print(f'default result: \u03C0 * {radius}^2 = {area_rounded}m^2')# Only display result

def rectangle_area(mode):
    length=float(input("what is the length of the rectangle? "))
    width=float(input("what is the width of the rectangle? "))
    #radius_float=float(radius)
    area= length * width # calculation came from my brain
    area_rounded= round(area, 1) # rounds the result to one decimal place   
    if mode == 'v':
        print(f'equation result: {length} * {width} = {area_rounded}  (length * width = area)')# Display formula and result
        
    else:
        print(f'default result: {length} * {width} = {area_rounded}')# Only display result

def cylinder_volume():
    print("cylinder calc")

def triangle_area():
    print("triangle calc")

def circle_volume():
    print("circle volume calc")



def main(): # function for the main program to be used with pytest
    
    mode = 'd' # start off the display in the default view

    while True: # main loop of the program
        print('''
    A/V calculator


Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view or D/d for default view.

	
    1.	Area of a circle calulation
    2.	Area of a rectangle calculation
    3.	Volume of a cylinder calculation
    4.	Area of a triangle calculation
    5.	Fifth Area/Volume* calculation''')
    
    
        level_0_1 = input("Please provide an input: ")
    
        if (level_0_1.lower()=='q'):
            exit('thanks for using this calculator') # when q is entered the program exits with an exit message
        
        elif (level_0_1.lower()=='v'):
            selected_mode('v') # sends v to the function selected_mode
            print('\nEquation View')
        
    
        elif (level_0_1.lower()=='d'):
            selected_mode('d') # sends d to the function selected_mode
            print('\nDefault View')
        
        elif (level_0_1=='1'):
            circle_area(mode)
            #print('1')
    
        elif (level_0_1=='2'):
            rectangle_area(mode)
            print('2')
        
        elif (level_0_1=='3'):
            print('3')
        
        elif (level_0_1=='4'):
            print('4')
        
        elif (level_0_1=='5'):
            print('5')

if __name__ == "__main__": # to be used with pytest
    main()
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    

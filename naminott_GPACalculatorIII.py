import naminott_GPA_BR

#Nakayla Minott, Jul 24, 2022
#Class Section COMP163001.202240

# This is a dynamic GPA Calculator used to display each semsters GPA, honors, major, and cumulcative GPA.
# using functions, if, and while statements.




print('Welcome to The GPA Calculator.')
print('This GPA calculator will help you calculate your Major, Honors, and Semester GPA.')

print('For the GPA calculator you will be entering quality points.')

print('Quality pointsA = 4 A- = 3.7 b+ = 3.3 B = 3 B- = 2.7 C+ = 2.3 C =2.3 C- = 1.7 D+ = 1.3 D = 1 F = 0')

# While statement to choose which what GPA to calculate.
# this is a menu for the calc
def calc_menu():
    print('If Honors print 1')
    print('If Major print 2')
    print('if Semesters print 3')
    print('If Cumulative print 4')
    print('Enter Q to quit: ')

#while function for menu to work with BR    
while True:
    calc_menu() 
    Input_for_menu = input("What would you like to calculate ?  ").upper()
    if Input_for_menu == "1":
        naminott_GPA_BR.Honors_GPA()

    elif Input_for_menu == "2":
         naminott_GPA_BR.Major_GPA()

    elif Input_for_menu == "3":
        naminott_GPA_BR.Semester_GPA()
        
    elif Input_for_menu == "4":
        naminott_GPA_BR.Cumulative_GPA()    
    else:
        Input_for_menu == 'Q'
        naminott_GPA_BR.Quit()



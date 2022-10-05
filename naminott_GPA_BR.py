
#Nakayla Minott, Jul 24, 2022
#Class Section COMP163001.202240

# This is a dynamic GPA Calculator used to display each semsters GPA, honors, major, and cumulcative GPA.
# using functions, if, and while statements.

#  Major GPA variables
Major_Quality_Points = []
Major_Class_Credits= []
Major_Credit_Multiple = []
Major_GPA = ''

# Honor_GPA variables
Honor_Quality_Points = []
Honor_Class_Credits = []
Honor_Credit_Multiple =[]
Honors_GPA = ''

# Semester GPA Variables
Semester_Quality_Points = []
Semester_Class_Credits = []
Semester_Credit_Multiple = []
Semester_GPA = ''

#function for Major GPA




def Major_GPA():

    # calc for Major GPA
    # for major GPA you need the number of classes you've taken for your college major
    # take the quality points you recevied for the class and the credits that class is worth then multiply them
    # after multiplying that number for each class divide the sum of the credit multipe by the sum of the class credits.

    print('Time to calculate your Major GPA.')
    print('Major GPA is a measure of your average scores only in the courses which contribute to your major degree.')

    Major_Class_num = int(input('Enter the number of classes you took for your Major thus far:'))

    for i in range(0, Major_Class_num):
        Major_Quality_Points.append(float(input(f"Enter the points you recevied for class {i+1}: ")))
        Major_Class_Credits.append(float(input(f"Enter the Credits that class {i+1} qualifies for: "))) 
        Major_Credit_Multiple.append(Major_Quality_Points[i] * Major_Class_Credits[i]) 
        Major_GPA = sum(Major_Credit_Multiple)/sum(Major_Class_Credits)

    print(f'Your Major GPA is {Major_GPA:.2f}')    
   
#function for Honors GPA

def Honors_GPA():
   #calc for Honors GPA
    # for honors GPA you need the number of classes you've taken during your college career
    # and take the quality points and class credits multiply them and then divide the sum of that 
    # by the sum of the class credits.

    print('Time to calculate your Honors GPA.')
    print('Honors GPA is a calculation of all the class you have taken.')
        
    Class_num = int(input('Enter the number of classes you took during your college career: '))
        
    for i in range(0, Class_num):
        Honor_Quality_Points.append(float(input(f"Enter the points you recevied for class {i+1}: ")))
        Honor_Class_Credits.append(float(input(f"Enter the Credits that class {i+1} qualifies for: "))) 
        Honor_Credit_Multiple.append(Honor_Quality_Points[i] * Honor_Class_Credits[i]) 
        Honors_GPA = sum(Honor_Credit_Multiple)/sum(Honor_Class_Credits)

    print(f'Your Honors GPA is {Honors_GPA:.2f}')   

#function for Semester GPA

def Semester_GPA():
    #calc for Semester GPA
    # for Semester GPA you first need to know the number of semesters the student has gone through
    # then you need to know the number of classes you have taken during those semesters
    # for each semester you need to take the quality pints you recived in those classes and the credits those class are worth
    # then multiply them after that take the sum of the multiplied and then divide that by the sum of class credits.


    print('Time to calculate your GPA per Semester.')
    print('Semester GPA is calculated by multiplying the number of credit hours assigned to a course by the value of the grade earned in that semester.')

    Sem_num = int(input('Enter the number of semesters you have gone though: '))

    for i in range(0, Sem_num):
        Num_class_Sem = int(input(f'Enter the number of class you took during this semester {i+1}:'))
        for u in range(0,Num_class_Sem):
            Semester_Quality_Points.append(float(input(f"Enter the points you recevied for class {u+1}: ")))
            Semester_Class_Credits.append(float(input(f"Enter the Credits that class {u+1} qualifies for: "))) 
            Semester_Credit_Multiple.append(Semester_Quality_Points[u] * Semester_Class_Credits[u]) 
            Semester_GPA = sum(Semester_Credit_Multiple)/sum(Semester_Class_Credits)  

        print(f'Your Semester GPA is {Semester_GPA:.2f}')

def Cumulative_GPA():

    #calc for Cumulative GPA
    # for cumulative GPA you need to know the number for class a student has taken during their college career
    # then you need to take out any duplicates     
    # then take the quality points you recived for those classes and the credits they are worth and multiply them
    # then multiply them after that take the sum of the multiplied and then divide that by the sum of class credits.
    
    print('Time to calculate your Cumulative GPA.')
    print('Cumulative GPA is a calculation of all your class without duplicates.')

    num_cumulative_class = int(input('Enter the number of class you have taken during your college career : '))
    names = []
    cumulative_class_credits = []
    cumulative_quality_points = []
    GPA = []
    cumulative_GPA = ''

    for i in range(0, num_cumulative_class): 
        class_names = (input(f'Enter the name of the class {i+1}: '))
        class_grades = float(input(f'Enter the points you recevied for class {i+1}: '))
        class_hours = float(input(f'Enter the Credits that class {i+1} qualifies for: '))
        if class_names in names:
            j = names.index(class_names)
            if class_grades > cumulative_quality_points [j]:
                cumulative_quality_points [j] = class_grades
                cumulative_class_credits [j] = class_hours
        else:
            names.append(class_names)    
            cumulative_quality_points.append(class_grades)  
            cumulative_class_credits.append(class_hours)  
    for i in range(len(names)):
        GPA.append(cumulative_class_credits[i]* cumulative_quality_points[i])

    cumulative_GPA = sum(GPA)/sum(cumulative_class_credits) 

    print(f'Your cumulative GPA is {cumulative_GPA:.2f}') 


def Quit():
    print('closing Program!!')
    quit()

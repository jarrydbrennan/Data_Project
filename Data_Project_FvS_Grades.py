#Write a program that reads in the csv file
#Outputs mean, median, & standard deviation for fall & spring semesters
#Jarryd Brennan

#file structure: firstname lastname,semester year, grade
#loop through file create a dictionary for each semester and assign then operate on values
#names are currently irrelevant

import statistics
semester_data = {}
#file = "sample_grades.csv"

def student_data(file):
    for line in open(file):
        name, semester, grade = line.strip().split(",") #.strip removes white space
        grade = float(grade)
        if semester not in semester_data: # this line checks if the dictionary contains information
        # about the current semester. If it doesn't, it adds a new entry for that semester in the dictionary
        # with some initial values vv.
            semester_data[semester] = {'grades': [], 'total_students':0, 'total_grade': 0.0}
        semester_data[semester]['grades'].append(grade)
        semester_data[semester]['total_students'] +=1
        semester_data[semester]['total_grade'] += grade

def calc_n_print():
    for semester, data in semester_data.items(): #key, value
        grades = data['grades']
        total_students = data['total_students']
        total_grade = data['total_grade']

        average_grade = total_grade / total_students
        median_grade = statistics.median(grades)
        std_deviation = statistics.stdev(grades)

        semester_data[semester]['average_grade'] = average_grade
        semester_data[semester]['median_grade'] = median_grade
        semester_data[semester]['std_deviation'] = std_deviation

    for semester, data in semester_data.items():
        total_students = data['total_students']
        average_grade = round(data['average_grade'], 2)
        median_grade = data['median_grade']
        std_deviation = round(data['std_deviation'], 2)
        print(semester,"\n"+"Average grade:",average_grade,"\n"+"Median grade:", median_grade,"\n"+"STD:", std_deviation)
        #print(median_grade)
        #print(std_deviation)

def main():
    student_data("sample_grades.csv")
    calc_n_print()

main()
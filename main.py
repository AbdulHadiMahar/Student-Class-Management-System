import os
import json
students = []
students_object = {}
class Student:
    def __init__(self,name , roll , mmarks,pmarks,cmarks):
        self.name = name
        self.roll = roll
        self.mmarks = mmarks
        self.pmarks = pmarks
        self.cmarks = cmarks
    def showdetails(self):
        print(f'{self.name} has a roll number {self.roll}')
        print(f'{self.mmarks} Maths marks, {self.pmarks} marks in Physics,'
        f'{self.cmarks} marks'  in Computer')

    def result(self):
        self.percentage = (((self.mmarks + self.cmarks + self.pmarks)/300)*100 ) 
        self.total = self.mmarks + self.cmarks + self.pmarks

    def showresult(self):
        return (f'The student got \n'
            f'Marks {self.mmarks} in Maths \n'
            f'Marks {self.pmarks} in Physics \n'
            f'Marks {self.cmarks} in Coputer \n'
            f'Total Marks {self.total} out of 300 \n' \
            f'Percentage {self.percentage}%\n' )

def load_data():
     if os.path.exists('Studentclass.txt'):
         with open('Studentclass.txt', 'r')as z:
            data = json.load(z)
         for name, student in data.items():
            student1 =  Student(
                student['name'],
                student['roll'],
                student['mmarks'],
                student['pmarks'],
                student['cmarks'],   
            )  
            students_object[name] = student1 
            students.append(name)    

def menu():
    try:
        return int(input("\nPress 1 to add a student \n"
            "Press 2 to view all students \n" 
            "Press 3 to search marks of student by roll number \n" 
            'Press 5 to update marks of student bu roll number \n' \
            'Press 6 to get a result of student by roll number \n' \
            'Press 9 to terminate a student from class by roll number\n'
            "Press 0 to exit : "))
    except ValueError:
        print("Entre a valid integer")

load_data()
while True:
    m = menu()
    match m:
        case 1:
             nm = input('Entre the name of student : ')
             rl = int(input('Entre the roll number of student : '))
             mm = int(input('Entre the marks of Maths out of 100 : '))
             pm = int(input('Entre the marks of Physics out of 100 : '))
             cm = int(input('Entre the marks of Computer out of 100 : '))
             student1 = Student(nm,rl,mm,pm,cm)
             students.append(nm)
             students_object[nm] = student1
             print('The student is added in Class')

        case 2:
            if len(students) == 0:
                print('There are 0 student in class')
            else:
                print(f'There are {len(students)} in class')
                for i in students_object.values():
                 Student.showdetails(i)
                 print('')

        case 3:
            s = int(input('Entre the roll number of student you want to search : '))
            for name, student in students_object.items():
                if student.roll == s:
                  student.showdetails()
                  break
            else:
               print(f'There is no student with roll number {s}')

        case 5:
            mr = int(input('Entre the roll number of student you want to update marks : '))
            for name, student in students_object.items():
                 if student.roll == mr:
                    upm = int(input('Entre 1 to change Math marks, Press 2 to change Phycics marks, or press 3 to change Computer marks'))
                    match upm:
                        case 1:
                            mathm=int(input('Entre the marks of Maths you want to change '))
                            student.mmarks = mathm
                            print('The marks is updated')
                        case 2:
                            physicsm=int(input('Entre the marks of Physics you want to change '))
                            student.pmarks = physicsm
                            print('The marks is updated')
                        case 3: 
                            computerm=int(input('Entre the marks of Computer you want to change '))   
                            student.cmarks = computerm
                            print('The marks is updated')
                        case _:
                            print('Entre a valid choice') 
            else:
                            print(f'There is no student with roll number {mr}') 

        case 6:
            getr = int(input("Entre the roll number : "))
            for name, student in students_object.items():
                if student.roll == getr:
                    student.result()
                    print(student.showresult())  
                    break
            else:
                print(f'There is no student with roll number {getr}')  
        case 9:
            ts = int(input('Entre the roll number of a student you want to terminate : '))
            for name, student in students_object.items():
                if student.roll == ts :
                 del students_object[name]
                 students.remove(name)
                 print(f"The student with roll number {ts} is terminated from Class")
                 break
            else:
                    print(f'There is no student with roll number {ts}') 
        case 0 :
            print('Saving Students data to ', os.path.abspath('Studentclass.txt'))
            with open('Studentclass.txt', 'w') as f:
                data = {}
                for name, student in students_object.items():
                    data[name] =  { 
                    'name' : student.name,
                    'roll' : student.roll,
                    'mmarks' : student.mmarks,
                    'pmarks' : student.pmarks,
                    'cmarks' : student.cmarks, 
                    }
                json.dump(data,f,indent=4)
            print('You are out')
            break          
        case _:
            print('Entre a valid choice')

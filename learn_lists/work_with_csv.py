# # Working with CSV without library
# students = []

# with open('students.csv') as file:
#     _ = file.readline()
    
#     for line in file:
#         parts = line.rstrip().split(',')
        
#         if len(parts) == 6:
#             student_id, student_name, exam_name, score, max_score, status = parts
            
#             student = {
#                 'student_id': student_id,
#                 'student_name': student_name,
#                 'exam_name': exam_name,
#                 'score': int(score),
#                 'max_score': int(max_score),
#                 'status': status
#             }
            
#             students.append(student)
        
# def calc_GP(score):
#     if not students:
#         return 0.0
#     gp = ((score * 5) / len(students)) * 1000
#     return gp

# for student in sorted(students, key=lambda x: x['student_name']):
#     gp_value = calc_GP(student['score'])
#     print(f"Name: {student['student_name']} has an ID of {student['student_id']} and has a GP of {gp_value:.2f} - {student['status']}")


# Reading using csv library
# import csv

# with open('students.csv', 'r') as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         print(f"{row['student_name']} scored {row['score']}/{row['max_score']} ({row['status']})")
       
       
        
# Appending using csv livrary
import csv

stud_id = input('Enter your ID: ')
name = input('Input your name: ')
exam = input('Input exam name: ')
score = input('Input score: ')
max_score = input('Input max score: ')
status = input('Input status (Passed/Failed): ')

with open('students.csv', 'a', newline='', encoding='utf-8') as file:
    # 1. Define the exact fieldnames matching your CSV header
    fieldnames = ['student_id', 'student_name', 'exam_name', 'score', 'max_score', 'status']
    
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # 2. Pass a dictionary. Notice the order here doesn't matter at all!
    writer.writerow({
        'student_name': name,
        'student_id': stud_id,
        'exam_name': exam,
        'score': score,
        'max_score': max_score,
        'status': status
    })

print("Student added successfully!")
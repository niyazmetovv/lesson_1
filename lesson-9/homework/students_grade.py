import csv

grades_data = {} # {subject : total_grade}
subjects_count = {} # {subject : count}

with open("grades.csv", 'r') as csvfile:
    content = csv.DictReader(csvfile)
    for row in content:
        subject = row['Subject']
        grade = float(row['Grade'])
        if subject in grades_data:
            grades_data[subject] += grade
            subjects_count[subject] += 1
        else:
            grades_data[subject] = grade
            subjects_count[subject] = 1

average_grades = {subject: round(grades_data[subject] / subjects_count[subject], 2) for subject in grades_data}

with open("average_grades.csv", 'w', newline='') as csvfile:
    header = ['Subject', 'Grade']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()
    for subject, avg in average_grades.items():
            writer.writerow({'Subject': subject, 'Grade': avg})

print("Successfully wrote average grades to csv file")
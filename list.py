def group_students_by_age(students):
    age_groups = {}  
    
    for student in students:
        age = student['age']
        name = student['name']
        
        if age in age_groups:
            age_groups[age].append(name)
        else:
            
            age_groups[age] = [name]
    
    return age_groups


students = [
    {'name': 'Alice', 'age': 20},
    {'name': 'Bob', 'age': 22},
    {'name': 'Charlie', 'age': 20},
    {'name': 'David', 'age': 22},
    {'name': 'Eve', 'age': 21}
]

grouped_students = group_students_by_age(students)

print(grouped_students)

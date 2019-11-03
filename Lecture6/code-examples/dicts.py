# I need a way to keep track of my students
my_students = {'Ayse': ['economics', 'freshman'],
                'Emir': ['psychology', 'master'],
                'Emirhan': ['business administration', 'junior'],
                'Furkan': ['law', 'junior'],
                'Mahsa': ['material science', 'phd'],
                'Meva': ['international relations', 'freshman']}

for student, info in my_students.items():
    print(f'{student} studies {info[0]}')
# Emir left my class :(
my_students.pop('Emir')
# someone new in my class
my_students['Canan'] = ['industrial engineering', 'junior'] 
# Ayse passed another year
my_students['Ayse'][1] = 'sophomore'

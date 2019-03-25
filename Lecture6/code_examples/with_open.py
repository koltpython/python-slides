f = open('my_file.txt', 'r') as f:
    # Content of my_file.txt: '1,0,2'
values = f.read().split(',')
# What happens
result = int(values[0]) / int(values[1]) + int(values[2])
f.close()

# Safer approach, file is closed
# even when we encounter an exception
with open('my_file.txt', 'w') as f:
    f.write('Hello, world!')

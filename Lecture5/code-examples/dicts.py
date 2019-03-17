d = {'x': 1, 'y': 2, 'z': 3}
for key, value in d.items():
    print(f'value {value} is associated with key: {key}')

for key in d:
    print(f'value {d[key]} is associated with key: {key}')

# Add new pairs
d['a'] = 15
# Change value of key
d['x'] = 1
# Remove pairs
y_value = d.pop('y')

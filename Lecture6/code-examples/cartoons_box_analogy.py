cartoon_characters = ['Tweety', 'Sponge Bob', 'Jerry', 'Minnie', 'Mickey', 'Sandy']

mickey_mouse = ['Minnie', 'Mickey']
sponge_bob = ['Sponge Bob', 'Sandy']
print(f'Characters in Mickey Mouse: {mickey_mouse}')
print(f'Characters in Sponge Bob: {sponge_bob}')

my_age = 9
my_age += 12
print(my_age)   # => 21

mickeys_leaving = cartoon_characters
mickeys_leaving.remove('Mickey')
mickeys_leaving.remove('Minnie')
print(cartoon_characters)     
# => ['Tweety', 'Sponge Bob', 'Jerry', 'Sandy']

my_secret_box = [0, 1, 2]
other_box = my_secret_box
other_box.remove(2)
print(my_secret_box)

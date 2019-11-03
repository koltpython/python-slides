ceren = {'Marco', 'Irem', 'Sunduz'}
gul_sena = {'Gamze', 'Ata', 'Zeynep'}
hasan_can = {'Gamze', 'Berker', 'Cemre'}
ahmet = {'Irem', 'Demet', 'Ekin'}

# intersection &
print(gul_sena.intersection(hasan_can))  # => {'Gamze'}
print(ceren & gul_sena)  # => set()
# union |
print(ceren.union(ahmet))  # => {'Ekin', 'Irem', 'Demet', 
                           # 'Marco', 'Sunduz'}
print(hasan_can | ceren | gul_sena | ahmet)  # => all names
# difference -
print((gul_sena - hasan_can))  # => {'Zeynep', 'Ata'}
# symmetric_difference ^
print(ceren.symmetric_difference(ahmet))
# => {'Marco', 'Ekin', 'Sunduz', 'Demet'}}

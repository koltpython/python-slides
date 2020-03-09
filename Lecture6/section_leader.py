ceren = ['şeref', 'şeref','oya', 'ata', 'simge', 'deniz']
haluk = ['matteo', 'hakan', 'tuan', 'mehmet', 'waseem']
ahmet = ['kutay', 'mine', 'fatma', 'nergis']
necla = ['göktuğ', 'beste', 'ilke']
ayse = ['sedef', 'elif', 'şakir', 'zeynep', 'şahin']
eralp = ['atahan', 'irem', 'ırmak', 'ahmet']
hasan = ['uğur', 'ismail', 'murat', 'tuğçe']
firat = ['ata', 'ömer', 'lara']
sections = [ceren, haluk, ahmet, necla, ayse, eralp, hasan, firat]

# number of unique names
all_students = set()
for section in sections:
    all_students = all_students | set(section)


print(all_students)


def find_section_leader_list(student_name):
    pass


section_dict = {
    'ceren': ['şeref', 'oya', 'ata', 'simge', 'deniz'],
    'haluk': ['matteo', 'hakan', 'tuan', 'mehmet', 'waseem'],
    'ahmet': ['kutay', 'mine', 'fatma', 'nergis'],
    'necla': ['göktuğ', 'beste', 'ilke'],
    'ayse': ['sedef', 'elif', 'şakir', 'zeynep', 'şahin'],
    'eralp': ['atahan', 'irem', 'ırmak', 'ahmet'],
    'hasan': ['uğur', 'ismail', 'murat', 'tuğçe'],
    'firat': ['ata', 'ömer', 'lara']
}


def find_section_leader_dict(section_info, student_name):
    pass

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# You may need to update file path!
mails = open('stud-mails.txt', 'r')
dict_majors = {}
dict_faculties = {}

for mail in mails:
    try:
        username = mail.split('@')[0]
        r = requests.get(
            f'http://ldap.ku.edu.tr/eGuide/servlet/eGuide?Action=Detail.get&User.dn=cn%3d{username}%2cou%3dSTD%2co%3dKU&Directory.uid=New_Data_Source')
        soup = BeautifulSoup(r.content, 'html.parser')
        values = soup.findAll('td', {'class': 'ValueText'})
        major = values[0].next

        if 'Master' in major or 'PHD' in major:
            faculty = major.split()[2]
        else:
            faculty = major.split()[1]

        if 'Student Electives General' in major:
            print('Electives general:', mail)
        else:
            # Append major
            if major in dict_majors:
                dict_majors[major] += 1
            else:
                dict_majors[major] = 1
            # Append faculty
            if faculty in dict_faculties:
                dict_faculties[faculty] += 1
            else:
                dict_faculties[faculty] = 1
    except:
        print(f'Exception in {mail}')

# majors = []
# counts = []

# for key in dict_majors:
#     majors.append(key)
#     counts.append(dict_majors[key])


# patches, texts = plt.pie(counts, shadow=False, startangle=90)
# plt.legend(patches, majors, loc="best")
# plt.axis('equal')
# plt.tight_layout()
# plt.show()


# print(dict_majors)

# fig1, ax1 = plt.subplots()
# ax1.pie(counts, labels=majors, autopct='%1.1f%%',
#         shadow=False, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# ax1.legend(patches, labels, loc="best")

# plt.show()

faculties = []
counts = []

for key in dict_faculties:
    faculties.append(key)
    counts.append(dict_faculties[key])

fig1, ax1 = plt.subplots()
ax1.pie(counts, labels=faculties, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')
plt.show()

print(dict_faculties)
print(dict_majors)

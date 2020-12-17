subj = {}
init_f = open('file_ex_6.txt', 'r')
for line in init_f:
    subject, lecture, practice, lab = line.split()
    subj[subject] = int(lecture) + int(practice) + int(lab)
print(f'Общее количество часов по предмету: {subj}')
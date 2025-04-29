lession1 = {
    'hour': '9:00',
    'topic': 'Microbiology',
    'teacher': 'Professor Wirus',
}
lession2 = {
    'hour': '12:00',
    'topic': 'Ethics',
    'teacher': 'doc. Kolba',
}
lession3 = {
    'hour': '14:00',
    'topic': 'Chemistry',
    'teacher': 'Professor Olej',
}

lession_list = [lession1, lession2, lession3]

lession_dict = {}
for lession in lession_list:
    lession_dict[lession['topic']] = lession

for topic, lession_info in lession_dict.items():
    print(topic, lession_info['hour'])
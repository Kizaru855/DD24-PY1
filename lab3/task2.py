def find_common_participants(group1, group2, divider=','):
    list1 = group1.split(divider)
    list2 = group2.split(divider)
    common_participants = list(set(list1).intersection(list2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, "|")
print(participants)

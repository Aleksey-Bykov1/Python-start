from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8') as user:
    user_list = [i.split(',') for i in user]

with open('hobbies.csv', 'r', encoding='utf-8') as hobbies:
    hobbies_list = [i.split(',') for i in hobbies]

if len(user_list) < len(hobbies_list):
    print('Process finished with exit code 1')
else:
    tmp = [i for i in zip_longest(user_list, hobbies_list)]
    dict_user = {}
    for i in tmp:
        dict_user.setdefault(str(i[0]).replace(',', ' ').replace('[', '').replace(']', '').replace(' ', '').replace("\\n", ''), i[1])
    for i, j in dict_user.items():
        with open('users_hobby.txt', 'a', encoding='utf-8') as us_ho:
            n = str(j)
            us_ho.writelines(f"{i}: {n.replace('[', '').replace(']', '')} \n")

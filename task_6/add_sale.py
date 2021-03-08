from sys import argv


with open('bakery.csv', 'a', encoding='utf-8') as add:
    add.writelines(f'{argv[1]} \n')



#if __name__ == '__main__':

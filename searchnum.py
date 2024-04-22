import re

found_num = open("found-num.csv", 'w')
filemy = r"C:\Users\Pavel Pablo\Desktop\SearchAndRecovery\tasks\1.2\text2.txt.res"

def find_phone_numbers(filemy):
    with open(filemy, 'r') as file:
        content = file.read()
        phone_numbers = re.findall(r"(\+7|8)[- _]*\(?[- _]*(\d{3}[- _]*\)?([- _]*\d){7}|\d\d[- _]*\d\d[- _]*\)?([- _]*\d){6})", content)
        return phone_numbers

phone_numbers = find_phone_numbers(filemy)

for number in phone_numbers:
    print(number)
    found_num.write(str(number) + '\n')

found_num.close()
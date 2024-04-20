found_numbers = open('file-numbers.csv', 'w')

filemy =r"C:\Users\Pavel Pablo\Desktop\SearchAndRecovery\tasks\1.1\phone_numbers.txt" 
info_to_exclude = "495"

def search_without_info(filemy, info_to_exclude):
    try:
        with open(filemy, 'r') as file:
            for line in file:
                if info_to_exclude not in line:
                    print(line)
                    found_numbers.write(line + '\n')
    except FileNotFoundError:
        print("not found.")
    except Exception as e:
        print("err:", e)

search_without_info(filemy, info_to_exclude)

found_numbers.close()
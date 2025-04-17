def create_phone_number(list):
    phone_number = '(xxx) xxx-xxxx'
    i = 0
    z = 1
    for i, numero in enumerate(list):
        while z != 13:
            if phone_number[z] == 'x':
                phone_number.replace(phone_number[z])
                i += 1
                z += 1
            else:
                z += 1
    
    print(list)
    print(phone_number)

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
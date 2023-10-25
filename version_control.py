def decode(password):
    """ 33332295 -> 00009962 """
    res = ''

    for char in password:
        n = int(char) - 3
        if n < 0:
            n = 10 + n
        
        res += str(n)
    
    return res


def encode(password):  # johnson nguyen
    encode = []
    password = list(password)
    password = [int(ele) for ele in password]
    for ele in password:
        encode.append(ele + 3)
    return encode


def main():
    menu = True
    while menu:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        menu_selection = int(input('Please enter an option: '))
        if menu_selection == 1:
            password = input('Please enter your password to encode: ')
            print(encode(password))
            print('Your password has been encoded and stored!')
        if menu_selection == 2:
            password = input('Please enter your password to decode: ')
            print(f'Decoded password is: {decode(password)}')
        if menu_selection == 3:
            exit()


if __name__ == '__main__':
    main()

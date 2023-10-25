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
            pass
        if menu_selection == 3:
            exit()


if __name__ == '__main__':
    main()

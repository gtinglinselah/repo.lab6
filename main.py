
def encoder(pass_code):
    password = ''
    for i in pass_code:
        i = int(i) + 3
        if i in range(0, 10):
            password += str(i)
        else:
            i %= 10
            password += str(i)
    return password


def menu():
    print('\nOption Menu',
          '-----------',
          '1. Encode Password',
          '2. Decode Password',
          '3. Exit', sep='\n')


def decoder(pw):
    pw_dec = ""
    for num in pw:
        num = int(num) - 3
        pw_dec += str(num)
    return pw_dec


if __name__ == "__main__":
    coder = True

    while coder:
        password = None
        menu()
        option = int(input('\nPlease enter an option: '))

        if option == 1:
            pass_code = str(input('Please enter your password to encode: '))
            pw_enc = encoder(pass_code)  # encoding password
            password = pw_enc  # storing encoded password
            print('Your password has been encoded and stored!')

        elif option == 2:
            pw_dec = decoder(pw_enc)
            # decode encoded password back to original using decode function
            print(f"the encoded password is {pw_enc}, and the original password is {pw_dec}.")

        elif option == 3:
            break

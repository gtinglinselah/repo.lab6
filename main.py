
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


if __name__ == "__main__":
    pass_code = str(input('Enter a password to encode: '))
    print(encoder(pass_code))

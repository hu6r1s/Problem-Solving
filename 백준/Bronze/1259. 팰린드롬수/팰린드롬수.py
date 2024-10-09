while True:
    string = input()

    if string == '0': break

    reversed_string = string[::-1]
    print("yes" if string == reversed_string else "no")
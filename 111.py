def program():
    girdi = int(input('Bir eded girin: '))
    if girdi % 2 == 1:
        print('Bu eded tekdir')
    else:
        print('bu eded tek deyil')
    if girdi % 2 == 0 and girdi != 0:
        print('bu eded cutdur')
    else:
        print('Bu eded cut deyil')
    if girdi == 0:
        print('bu eded ne tek ne de cutdur')


program()
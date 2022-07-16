def rain_sound():
    n = int(input('enter a number: '))

    if n%3 == 0 and n%5 == 0:
        print("pling plang")

    elif n%5 == 0 and n%7 == 0:
        print('Plang plong')

    elif n%3 == 0 and n%7 == 0:
        print('pling plong')

    elif n%3 == 0:
        print('pling')

    elif n%5 == 0:
        print('Plang')

    elif n%7 == 0:
        print('Plong')

    else:
        print
rain_sound()

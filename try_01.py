while True:
    print("press q to quit")
    a=input('Enter a number: ')
    if a=='q':
        print("you quit byeeee")
        break
    try:
        a=int(a)
        if a=='q':
            break

        if a>5:
            print("a is greater than 5")
    except Exception as e:
        print("sorry your input does not support this program")    

print("Thanks for playing this game")

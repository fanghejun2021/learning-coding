while True:
    reply = input("Enter a number bigger than 20: ")
    if reply == 'stop':
        break
    elif int(reply) < 20:
        print("number is less than 20")
    else:
        print('%d squared is %d' % (int(reply),int(reply)**2))


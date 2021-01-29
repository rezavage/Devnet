state = ''
prev =''
while True:
    state=input('>').upper()
    if state=='START':
        if state==prev:
            print ('the car is already started')
        else:
            print('The car is started')
            prev=state
    elif state=='STOP':
        if state==prev:
            print('the car is already stopped')
        else:
            print('the car is stopped')
            prev=state
    elif state=='HELP':
        print('''
start
stop
help
quit''')
    elif state=='QUIT':
        break
    else:
        print('Unknown Command')

else:
    print('bye')
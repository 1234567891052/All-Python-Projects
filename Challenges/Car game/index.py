n = input('Enter a command: ') 
operations = {
    'help' : 'Tells you about the commands', 
    'start' : 'Starts the car',
    'stop' : 'Stops the car',
    'quit' : 'Quit application'
}
while n != 'quit' :
    if n == 'help' : 
        for i in operations :
            print(i + ': ' + operations[i])
        n = input('Enter a command: ') 
    elif n == 'start' :
        print('The car has started...')
        n = input('Enter a command: ') 
    elif n == 'stop' :
        print('The car has stopped')
        n = input('Enter a command: ') 
    else :
        print('ERR IN COMMAND')
        n = input('Enter a command: ') 
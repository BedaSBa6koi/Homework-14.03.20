fahr = print('Enter the desired number and F if you want to convert Fahrenheit to Celsius\n')
cels = print('Enter the desired number and C if you want to convert Celsius to Fahrenheit\n')
t = (input('Enter: \n'))
sign = t[-1]
t = int(t[0:-1])

def calc(t):
    if sign == 'C' or sign == 'c':
        t = int(t * (9/5) + 32)
        print(str(t) + 'F')
    elif sign == 'F' or sign == 'f':
        t = int((t - 32) * (5/9))
        print(str(t) + 'C')    

(calc(t))
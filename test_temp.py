temp = input('Температура ')
conv_choise = input('Если С в F, ввод f и наоборот')

def c_to_f(temperature):
    return (temperature * 9/5) + 32

def f_to_c(temperature):
    return (temperature - 32) * 5/9

def conv_temp
    if conv_choise == 'f':
        print(c_to_f)
    else:
        print(f_to_c)

convert_
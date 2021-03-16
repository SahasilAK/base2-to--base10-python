def base2_ValueGenerator(val):
    run = True
    quo = val
    base2_val = ''
    while run:
        rem = quo%2
        quo = int(quo/2)
        base2_val = str(rem) + base2_val
        if quo == 0 or quo == 1:
            base2_val = str(quo) + base2_val
            run = False
    return base2_val
def base10_ValueGenerator(val):
    #int has no len so this way is better
    base10_val = sum(int(val[i])*2**(len(val)-i-1) for i in range(0,len(val)))
    return base10_val
def start_prog():
    user_input = input('Enter your choice:\n1 - base2 to base10\n2 - base10 to base2\n')
    if user_input == '1':
        base2_val = input('Enter the base2 value:\t')
        print(base10_ValueGenerator(base2_val))
    elif user_input == '2':
        base10_val = int(input('Enter the base10 value:\t'))
        print(base2_ValueGenerator(base10_val))
    else:
        print("Wrong Choice Try again!!")
        start_prog()
start_prog()

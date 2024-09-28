'''
Implementation of Bolzano's theorem

"If a function, f(x), defined on an interval [a, b] is continuous && f(a) * f(b) == 0 -->
--> there's a number c, in (a, b) / f(c) = 0"
'''

def main() -> None:
    function1 = define_function()
    function2 = define_function()
    try:
        interval = input('Insert the interval [2 number separated by spacebar]>').split(' ')
        
        # Iterates and converts in a float type all the elemenents of interval
        i = 0
        while i < len(interval):
            interval[i] = float(interval[i])
            i += 1
        interval:tuple = tuple(interval)
    
    except:
        print('Error')


def define_function() -> dict:
    '''
    Key:degree value:number
    It creates a dictionary with the values of the degree of the variable and its value.
    '''
    function:dict = {}
    user_in:str = ''

    while True:
        try:
            user_in:str = str(input('Insert the degree of the variable [q - exit]>'))
            if user_in.lower() != 'q':
                int(user_in) # To prove type validity
                function[user_in] = int(input('Insert the value of the variable>'))
            else:
                break  
        except:
            print('Error')
        
    return function


if __name__ == '__main__':
    main()

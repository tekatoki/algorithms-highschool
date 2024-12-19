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
        
        precision:int = input('How precise do you want the program to be [insert a number]>')
    except:
        print('Error')
    

    # Starts Bolzano's theorem
    var_value:list = list(interval).sort()
        
    if ( calculation_func_value(function1, var_value[0]) or calculation_func_value(function2, var_value[1]) ) == 0:
        # Case that we already know that one function == 0
        if calculation_func_value(function1, var_value[0]) == 0:
            print(f'f(x) = 0 when x = {var_value[0]}')
        elif calculation_func_value(function2, var_value[1]):
            print(f'g(x) = 0 when x = {var_value[1]}')
        
    
    if calculation_func_value(function1, var_value[0]) * calculation_func_value(function2, var_value[1]) < 0:
        # Is possible to apply the theorem
        while calculation_func_value(function1, var_value[0]) * calculation_func_value(function2, var_value[1]) < 0:
            var_value[0] -= 1 / (10 ** precision)
            var_value[1] -= 1 / (10 ** precision)
            
        print(f"There is c in ({var_value[0], var_value[1]}) = 0")
    
    else:
        print("It's not possible to apply Bolzano's theorem")

def calculation_func_value (func:dict, var_value:float) -> float:
    '''
    Calculates de value of f(x). var_value is the value for x. Returns the result of the function.
    '''
    
    temp_result:float = 0 # stores the calculations 
    for key in func:
        temp_result += ( (func[key]) * (var_value ** int(key)) ) # a{func[key]} * x{var_value} ** n
    
    return temp_result # f(x)

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

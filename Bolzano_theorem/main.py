'''
Implementation of Bolzano's theorem

"If a function, f(x), defined on an interval [a, b] is continuous && f(a) * f(b) == 0 -->
--> there's a number c, in (a, b) / f(c) = 0"
'''

def in_functions() -> dict:
    '''
    Asks on the terminal for two functions and returns these as dict.
    key:degree value:number(int)
    '''
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
    
    function1:dict = define_function()
    function2:dict = define_function()
    



if __name__ == '__main__':
    in_functions()

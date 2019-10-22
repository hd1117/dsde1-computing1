def prod(first,second):
    '''
    The Docstring
    '''
    user_input=input('Enter a number: ')
    user_input2=input('Enter a second number: ')
    my_final_product = times(user_input, user_input2)
    return

def times(one, two):
    product = (one*two)
    return product

def __main__:
    '''
    The Main Function
    '''
    prod()
    return

if __name__ == '__main__':
    main()
#! /usr/bin/env python3
'''
This is a very faulty progamma.
Please keep Errors.py in the same directory when running script
Errors implemented to crash the program:

SyntaxError
ZeroDivisionError
UnboundLocalError
KeyError
FileNotFoundError
NameError
ModuleNotFoundError
IndexError
TypeError
RecursionError

'''

# Metavariables
__author__ = 'James Gray'

# Imports
import sys
import time

# Functions
def get_error():
    '''Get a list of errors for a user to try'''
    error_dict = {}
    for item in dir(__builtins__):
        if 'Error' in item:
            error_dict[item] = getattr(__builtins__, item).__doc__
    return error_dict

def return_error(error_dict):
    '''this function returns a list of invokeable errors'''
    for error in sorted(error_dict.keys()):
        print(error)
    
    print()
    error = input(
        "Please enter the error you're interested in to invoke error: ",).split()
    for step in error:
        if step in error_dict:
            print(step, '\n', error_dict[step], '\n')
        else:
            # Function calls itself again
            print('\n','You entered a non-existent Python Error: ','\n')
            print('Restarting script...','\n')
            time.sleep(3)
            return_error(error_dict)
    return error

def invoke_syntax_error(error):
    '''This function invokes a SyntaxError'''
    if len(error) == 1 and 'SyntaxError' in error:
        from Errors import syntax_error

def invoke_0_division(error):
    '''This function invokes a ZeroDivisionError'''
    if len(error) == 1 and 'ZeroDivisionError' in error:
        x = 3
        y = x/0

def invoke_UnboundLocalError(error):
    '''This function invokes a UnboundLocalError'''
    if len(error) == 1 and 'UnboundLocalError' in error:
        x+=1

def invoke_KeyError(error):
    '''This function invokes a KeyError'''
    if len(error) == 1 and 'KeyError' in error:
        x = {'B':420}
        print(x['C'])

def invoke_FNF_error(error):
    '''This function invokes a FileNotFoundError'''
    if len(error) == 1 and 'FileNotFoundError' in error:
        x = open('NSA_secrets.cleartxt')

def invoke_name_error(error):
    '''This function invokes a NameError'''
    if len(error) == 1 and 'NameError' in error:
        invoke_NASTY_error(error)

def invoke_module_not_found(error):
    '''This function invokes an ImportError'''
    if len(error) == 1 and 'ModuleNotFoundError' in error:
        import Vodka

def invoke_index_error(error):
    '''This function invokes an IndexError'''
    if len(error) == 1 and 'IndexError' in error:
        lst = [0,1,2,3,4,5]
        print(lst[6])

def invoke_type_error(error):
    if len(error) == 1 and 'TypeError' in error:
        x = 'áaaa'/3
        return

def invoke_recursion_error(error):
    invoke_recursion_error(error)
    if len(error) == 1 and 'RecursionError' in error:
        invoke_recursion_error(error)
        return   

# Main
def main(argv):
    # Preparation
    error_dict = get_error()
    error = return_error(error_dict)

    # Work
    invoke_syntax_error(error)
    invoke_0_division(error)
    invoke_UnboundLocalError(error)
    invoke_KeyError(error)
    invoke_FNF_error(error)
    invoke_name_error(error)
    invoke_module_not_found(error)
    invoke_index_error(error)
    invoke_type_error(error)
    invoke_recursion_error(error)
    return 0

if __name__ == '__main__':
    exitcode = main(sys.argv)
    sys.exit(exitcode)
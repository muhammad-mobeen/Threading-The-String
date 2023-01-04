'''
Author: Muhammad Mobeen
Reg No: 200901097
BS-CS-01  (B)
OS Assignment # 4
Submitted to Mam Asia Aman & Mam Reeda Saeed

GitHub Repo URL: https://github.com/muhammad-mobeen/Threading-The-String
'''
import threading

class StringThreader:
    '''
    Implements the following functions with dedicated threads:-
    1. Input String Thread
    2. Reverse String Thread
    3. Capitalize String Thread
    4. Shift String Thread

    Uses 'threads_driver' function as the main driver function for the whole operation.
    '''
    def __init__(self):
        self.istring = None  # Stores the input string

    def threads_driver(self):
        '''Defines the threads and drives them by starting and joining each thread according to the required logic'''
        input_thread = threading.Thread(target=self.input_string)
        reverse_thread = threading.Thread(target=self.reverse_string)
        capital_thread = threading.Thread(target=self.capitalize_string)
        shift_thread = threading.Thread(target=self.shift_string)

        input_thread.start()
        input_thread.join()
        if self.istring:
            reverse_thread.start()
            capital_thread.start()
            shift_thread.start()
            reverse_thread.join()
            capital_thread.join()
            shift_thread.join()

    def input_string(self):
        '''Inputs string from the user with some Exception Handling'''
        try:
            print("Please enter a string: ",end="")
            self.istring = input()
        except Exception as e:
            print("\n[!] Error occured while taking string input\nDetails: {}".format(e))

    def reverse_string(self):
        '''Reverses the input string and displays it in ouput'''
        rev_string = self.istring[::-1]
        print("Reversed String: {}".format(rev_string))

    def capitalize_string(self):
        '''Capitalizes the input string and displays it in ouput'''
        cap_string = self.istring.upper()
        print("Capitalized String: {}".format(cap_string))

    def shift_string(self):
        '''Shifts the input string character by character and displays it in ouput'''
        shifted_string = ''.join(chr(ord(s)+2) for s in self.istring)   # Using String Comprehensions
        print("Shifted String: {}".format(shifted_string))


if __name__ == '__main__':
    st = StringThreader()   # Intiate Class Object
    st.threads_driver()     # Start Operation
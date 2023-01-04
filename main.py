import threading

class StringThreader:
    def __init__(self):
        self.istring = None

    def threads_driver(self):
        input_thread = threading.Thread(target=self.input_string)
        reverse_thread = threading.Thread(target=self.reverse_string)
        capital_thread = threading.Thread(target=self.capitalize_string)
        shift_thread = threading.Thread(target=self.shift_string)

        input_thread.start()
        input_thread.join()
        reverse_thread.start()
        capital_thread.start()
        shift_thread.start()

        reverse_thread.join()
        capital_thread.join()
        shift_thread.join()

    def input_string(self):
        print("Please enter the string: ",end="")
        self.istring = input()

    def reverse_string(self):
        rev_string = self.istring[::-1]
        print("Reversed String: {}".format(rev_string))

    def capitalize_string(self):
        cap_string = self.istring.capitalize()
        print("Capitalized String: {}".format(cap_string))

    def shift_string(self):
        shifted_string = ''.join(chr(ord(s)+2) for s in self.istring)
        print("Shifted String: {}".format(shifted_string))


if __name__ == '__main__':
    st = StringThreader()
    st.threads_driver()
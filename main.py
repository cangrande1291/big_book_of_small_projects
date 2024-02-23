

class Cypher():

    shift_array = []

    def __init__(self, key, message):
        self.key = key
        self.message = message

    def encrypt(self):
        
        message_lenght = len(self.message)
        

        for letter in self.key:
            shift_value = ord(letter) - ord('a')
            self.shift_array.append(shift_value)

        print(self.shift_array)

        counter = 0
        new_string = []

        for letter in self.message:
            new_char = chr(ord(letter) + self.shift_array[counter])
            new_string.append(new_char)

        print(new_string)
        self.encrypted_string = 

    def decrypt(self):

        message_lenght = len(self.message)
        

        for letter in self.key:
            shift_value = ord(letter) - ord('a')
            self.shift_array.append(shift_value)

        print(self.shift_array)

        counter = 0
        new_string = []

        for letter in self.message:
            new_char = chr(ord(letter) + self.shift_array[counter])
            new_string.append(new_char)

        print(new_string)
            

obj = Cypher("la mia macchina è blu", "mi piace la bamba")
obj.encrypt()

from script import * # script.py functions
direction = input("For encode write enc and for decpode write dec: ")
text = input("Write the morse code or original text: ")
Data = Morse_code(text)
if direction == "enc": 
    print(Data.Encode()) 
elif direction == "dec": 
    answer = Data.Decode()
else: print("Your answer is not correct!")
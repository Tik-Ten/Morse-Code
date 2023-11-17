from script import * # script.py functions
direction = input("For encode write enc and for decpode write dec: ").lower()
text = input("Write the morse code or original text: ").lower()
Data = Morse_code(text)
if direction == "enc": print(Data.Encode()) 
elif direction == "dec": print(Data.Decode())
else: print("Your answer is not correct!")
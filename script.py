Morse_Letters = {
    "`" : "`",
    "!" : "!",
    "@" : "@",
    "#" : "#",
    "$" : "$",
    "%" : "%",
    "^" : "^",
    "&" : "&",
    "*" : "*",
    "(" : "(",
    ")" : ")",
    "-" : "-",
    "_" : "_",
    "+" : "+",
    "=" : "=",
    "/" : "/",
    "?" : "?",
    "~" : "~",
    "." : ".",
    "<" : "",
    ">" : "",
    " " : " ",
    "a" : ".-", 
    "b" : "-...", 
    "c" : "-.-.", 
    "d" : "-..", 
    "e" : ".", 
    "f" : "..-.", 
    "g" : "--.", 
    "h" : "....", 
    "i" : "..", 
    "j" : ".---", 
    "k" : "-.-", 
    "l" : ".-..", 
    "m" : "--", 
    "n" : "-.", 
    "o" : "---", 
    "p" : ".--.", 
    "q" : "--.-", 
    "r" : ".-.", 
    "s" : "...", 
    "t" : "-", 
    "u" : "..-", 
    "v" : "...-", 
    "w" : ".--", 
    "x" : "-..-", 
    "y" : "-.--", 
    "z" : "--.."
}
Morse_Letters_rev = {value: key for key, value in Morse_Letters.items()}
Letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
class Morse_code():
    def __init__(self, Text):
        self.text = Text
    def Encode(self): 
        text = ""
        for i in range(len(self.text)):
            try:
                text += Morse_Letters[self.text[i]]
            except:
                text += " <Invalid letter> "
        return text
    def Decode(self): 
        for i in range(len(self.text)):
            pass
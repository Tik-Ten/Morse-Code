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
    "a" : "._", 
    "b" : "_...", 
    "c" : "_._.", 
    "d" : "_..", 
    "e" : ".", 
    "f" : ".._.", 
    "g" : "__.", 
    "h" : "....", 
    "i" : "..", 
    "j" : ".___", 
    "k" : "_._", 
    "l" : "._..", 
    "m" : "__", 
    "n" : "_.", 
    "o" : "___", 
    "p" : ".__.", 
    "q" : "__._", 
    "r" : "._.", 
    "s" : "...", 
    "t" : "_", 
    "u" : ".._", 
    "v" : "..._", 
    "w" : ".__", 
    "x" : "_.._", 
    "y" : "_.__", 
    "z" : "__.."
}
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
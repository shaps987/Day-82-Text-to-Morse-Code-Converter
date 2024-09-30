MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '\'': '. _ _ _ .',
    '!': '_ . _ . _ _',
    '/': '_ . . _ .',
    '(': '_ . _ _ .',
    ')': '_ . _ _ . _',
    '&': '. _ . . .',
    ':': '_ _ _ . . .',
    ';': '_ . _ . _ .',
    '=': '_ . . . _',
    '+': '. _ . _ .',
    '-': '_ . . . . _',
    '_': '. . _ _ . _',
    '"': '. _ . . _ .',
    '$': '. . . _ . . _',
    '@': '. _ _ . _ .',
    ' ': '/'
}

class Encode:
    def __init__(self):
        self.text = input("Enter the text that you would like to encode into morse code: ")
        self.output = ""
        for char in self.text.upper():
            self.output += f"{MORSE_CODE_DICT[char]} "
        
        print(self.output)

class Decode:
    def __init__(self):
        self.text = input("Enter the morse code that you would like to deocde: ")
        self.output = ""
        self.text = self.text.split(" ")
        for string in self.text:
            self.output += f"{list(MORSE_CODE_DICT)[list(MORSE_CODE_DICT.values()).index(string)]}"

        self.output = self.output.lower()
        print(self.output)
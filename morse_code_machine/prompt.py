from morse_code_machine.conversion import Encode, Decode

class Prompt_User:
    def __init__(self, encode: Encode, decode: Decode):
        self.encode = encode
        self.decode = decode
        print("Welcome to the Morse Code Machine")
        self.encode_or_decode = input("Would you like to Decode or Encode Morse Code? ").lower()
        while self.encode_or_decode not in ["encode", "decode"]:
            print("Invalid Input")
            self.encode_or_decode = input("Would you like to Decode or Encode Morse Code? ")
        else:
            if self.encode_or_decode == "encode":
                self.encode()
            elif self.encode_or_decode == "decode":
                self.decode()

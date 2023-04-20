from pprint import pprint

ALPHABETH_PATH = "alphabeth.txt"

class Morse:
    def __init__(self) -> None:
        
        self.initiate_morse()


    def initiate_morse(self):
        """creates a morse dictionary"""

        with open(ALPHABETH_PATH) as file:
            alphabeth = file.readlines()
        alphabeth = [word.replace('\n', '') for word in alphabeth]
        self.alphabeth = {word.split("\t")[0]:word.split("\t")[1] for word in alphabeth}

    def translate_morse(self, sentence):
        """returns the morse code of the sentence"""
        morse_sentence = [f"{self.alphabeth[letter.upper()]}" if letter != ' ' else ' ' for letter in sentence]
        return morse_sentence


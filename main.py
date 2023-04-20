"""asks input from the user and prints out the morse code version of the sentence
The supported characters are in the alphabeth.txt file"""

from morse import Morse


morse = Morse()
sentence = ''
while sentence != 'stop':
    sentence = input("What sentence do you want to translate to morse code? (write stop to interrupt)\n").lower()

    morse_sentence = morse.translate_morse(sentence)
    for letter in morse_sentence:
        print(letter)
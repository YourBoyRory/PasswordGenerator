import random
import os
from wordlist import Wordlist
from config import Config as config

def clear_screen():
    if os.name == "posix":  # If we are on Linux or MacOS
        os.system('clear')
    else:                   # If we are on Windows
        os.system('cls')
    print(" ")

def format_keyphrase(random_word):
    new_random_word = ""
    for char in random_word:
        if char.isupper():
            new_random_word += '\033[4m\033[37m\033[1m' + char + '\033[0m'
        elif char.islower():
            new_random_word += '\033[37m' + char + '\033[0m'
        elif char.isdigit():
            new_random_word += '\033[36m\033[1m' + char + '\033[0m'
        else:
            new_random_word += '\033[31m\033[1m' + char + '\033[0m'
    return new_random_word+'\033[0m'

def generate_pin(mask):
    pin=""
    for char in mask:
        pin += str(random.randint(int(char), 9))
    return pin

def main():
     # Used to store the previously used words
     # avoids same words when generating multiple words and makes regens feel more random
    used_words = ["0"]*config.keyphrases

    clear_screen()
    wordlist = Wordlist(config)
    #wordlist.save_file()
    while True:
        for i in range(config.keyphrases):
            random_word=""
            for j in range(config.word_amount):
                while True: # Loop until we find a words that isnt in the used_words list
                    temp_word = random.choice(wordlist.wordlist).strip()
                    if random_word+temp_word not in used_words and temp_word not in random_word:
                        random_word += temp_word
                        if j+1 is not config.word_amount:
                            random_word += word_divider
                        break
            used_words[i] = random_word
            print("   \033[32m[",i+1,"]\033[0m", format_keyphrase(random_word+generate_pin(config.number_mask)+random.choice(config.sufix_selection)))
        input("\nPress Enter to regenerate...")
        clear_screen()

if __name__ == "__main__":
    main()

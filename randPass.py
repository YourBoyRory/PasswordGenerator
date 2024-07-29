import random
import os

 # Configure for use case
keyphrases=5               # amount of keyphrases to generate every time the user regens: 5
number_mask="0"*2          # Mask for the number generated. "0"*4 - 4 didgets 0-9, "1000" first diget is 1-9 last 3 are 0-9: "0"*4
filename ="words.txt"      # allowed word list file directory: words.txt
word_amount=1              # amount of words to be selected from the allowed word list: 1
word_divider=""            # divider that seperates each word in the keyphrase: ""
sufix_selection="!@#$%^&"  # Selects a random char from this string to sufix the keyphrase, use this if you need a special character "!@#$%^&".: " "
wordlist_required=True     # Do not use the default wordlist


        
def clear_screen():
    if os.name == "posix":  # If we are on Linux or MacOS
        os.system('clear')
    else:                   # If we are on Windows
        os.system('cls')
    print(" ")

 # Return complaint wordlist
def generate_wordlist(filename):
     # Used to store at least keyphrases+1 unique words
    compliant_words = ["0"]*int(keyphrases+1)
    default_wordlist = [
        "Apple", "Banana", "Mango", "Papaya", "Peach", "Orange", 
        "Grape", "Kiwi", "Lemon", "Melon", "Pineapple", "Plum",
        "Cherry", "Apricot", "Avocado", "Coconut", "Date", "Pomegranate",
        "Guava", "Lychee", "Nectarine", "Olive", "Pear", "Raspberry",
        "Strawberry"
    ]
    
     # if the word list is missing, use default
    try:
        with open(filename, 'r') as file:
            words = file.readlines()
    except:
        if wordlist_required:
            input("[ \033[31mFATAL\033[0m ] Wordlist is Required!")
            exit()
        else:
            print("[ \033[33mWARN\033[0m ] Using default wordlist\n")
            return default_wordlist
    
     # loops though the word list until it finds enough unique words
    count=0
    for word in words:
        if word not in compliant_words:
            compliant_words[count] = words[count]
            count=count+1
        if count is keyphrases+1:
            break
    # if count is not equal to keyphrases+1 then we looped the entire array without finding enough unique words
    if count is not keyphrases+1:
        print("[ \033[31mEROR\033[0m ] Wordlist is too short!")
        if wordlist_required:
            input("[ \033[31mFATL\033[0m ] Wordlist is Required!")
            exit()
        else:
            print("[ \033[33mWARN\033[0m ] Using default wordlist\n")
            return default_wordlist
    return words

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

def generate_pin_number(mask):
    pin=""
    for char in mask:
        pin += str(random.randint(int(char), 9))
    return pin

def main():
     # Used to store the previously used words
     # avoids same words when generating multiple words and makes regens feel more random
    used_words = ["0"]*keyphrases
    
    clear_screen()
    wordlist=generate_wordlist(filename)
    while True:
        for i in range(keyphrases):
            random_word=""
            for j in range(word_amount):
                while True: # Loop until we find a words that isnt in the used_words list
                    temp_word = random.choice(wordlist).strip() 
                    if random_word+temp_word not in used_words and temp_word not in random_word:
                        random_word += temp_word
                        if j+1 is not word_amount:
                            random_word += word_divider
                        break
            used_words[i] = random_word
            print("   \033[32m[",i+1,"]\033[0m", format_keyphrase(random_word+generate_pin_number(number_mask)+random.choice(sufix_selection)))
        input("\nPress Enter to regenerate...")
        clear_screen()

if __name__ == "__main__":
    main()

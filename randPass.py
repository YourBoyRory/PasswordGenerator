import random
import os

 # Configure for use case
word_count=5           # amount of words to generate every time the user regens: 5
number_mask="9"*4
filename = 'words.txt' # allowed word list file directory: words.txt
prefix=""
subfix=""

 # Return a random word form the allowed words list
def generate_wordlist(filename):
    with open(filename, 'r') as file:
        wordlist = file.readlines()
        return wordlist
        
def clear_screen():
    if os.name == "posix":  # If we are on Linux or MacOS
        os.system('clear')
    else:                   # If we are on Windows
        os.system('cls')
    print(" ")

 # Creates a compliant demo allowed words list
def make_compliant_wordlist(filename):
     # demo words
    wordlist = [
        "Apple", "Banana", "Mango", "Papaya", "Peach", "Orange", 
        "Grape", "Kiwi", "Lemon", "Melon", "Pineapple", "Plum",
        "Cherry", "Apricot", "Avocado", "Coconut", "Date", "Pomegranate",
        "Guava", "Lychee", "Nectarine", "Olive", "Pear", "Raspberry",
        "Strawberry"
    ]
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(word+"\n")
    print("[ \033[36mINFO\033[0m ] Generated new wordlist.","\n")

 # Returns true or false if the word list has enough words to allow no repeats for specified word_count
def check_wordlist_compliance(filename):
     # Used to store at least word_count+1 unique words
    compliant_words = ["0"]*int(word_count+1)
    
     # if the word list is missing, make a new one
    try:
        words = generate_wordlist(filename)
    except:
        make_compliant_wordlist(filename)
        return
    
     # loops though the word list until it finds enough unique words
    count=0
    for word in words:
        if word not in compliant_words:
            compliant_words[count] = words[count]
            count=count+1
        if count is word_count+1:
            break
    # if count is not equal to word_count+1 then we looped the entire array without finding enough unique words
    if count is not word_count+1:
        print("[ \033[33mWARN\033[0m ] The wordlist is too short!")
        make_compliant_wordlist(filename)
        return

def format_word(random_word):
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
        pin += str(random.randint(0, int(char)))
    return pin

def main():
     # Used to store the previously used words
     # avoids same words when generating multiple words and makes regens feel more random
    used_words = ["0"]*word_count
    
    clear_screen()
    check_wordlist_compliance(filename)
    wordlist=generate_wordlist(filename)
    while True:
        for i in range(word_count):
            while True: # Loop until we find a words that isnt in the used_words list
                random_word = random.choice(wordlist).strip() 
                if random_word not in used_words:
                    break
            used_words[i] = random_word
            format_word(random_word)
            print("   \033[32m[",i+1,"]\033[0m", format_word(prefix+random_word+generate_pin_number(number_mask)+subfix))
        input("\nPress Enter to regenerate...")
        clear_screen()

if __name__ == "__main__":
    main()

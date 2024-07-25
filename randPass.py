import random
import os

 # Configure for use case
word_count=5           # amount of words to generate every time the user regens: 5
filename = 'words.txt' # allowed word list file directory: words.txt

 # Used to store the previously used words
 # avoids same words when generating multiple words and makes regens feel more random
used_words = ["0"]*word_count

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

 # Returns true or false if the word list has enough words to allow no repeats for specified word_count
def check_wordlist_compliance(filename):
    compliant_words = ["0"]*int(word_count+1)
    try:
        with open(filename, 'r') as file:
            words = file.readlines()
    except:
        print("[\033[33mWARN\033[0m] Word list was missing, generated new one.","\n")
        make_compliant_wordlist(filename)
        return
        
    count=0
    for word in words:
        if word not in compliant_words:
            compliant_words[count] = words[count]
            count=count+1
        if count is word_count+1:
            break
    if "0" in compliant_words:
        print("[\033[33mWARN\033[0m] The wordlist was too short, generated new one.","\n")
        make_compliant_wordlist(filename)
        return
    

def main():
    clear_screen()
    check_wordlist_compliance(filename)
    wordlist=generate_wordlist(filename)
    while True:
        for i in range(word_count):
            random_number = random.randint(1000, 9999)
            while True: # Loop until we find a words that isnt in the used_words list
                random_word = random.choice(wordlist).strip() 
                if random_word not in used_words:
                    break
            used_words[i] = random_word
            print("   \033[37m\033[1m",random_word+"\033[36m"+str(random_number),"\033[0m")
        input("\nPress Enter to regen...")
        clear_screen()

if __name__ == "__main__":
    main()

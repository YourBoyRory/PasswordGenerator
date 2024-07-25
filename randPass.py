import random
import os

def generate_random_word(filename):
    with open(filename, 'r') as file:
        words = file.readlines()
        return random.choice(words).strip()

word_count=5
used_words = ["0"]*word_count
filename = 'words.txt'
if not os.path.exists(filename):
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

while True:
    if os.name is "posix":
        os.system('clear')
    else:
        os.system('cls')
    print(" ")
    for i in range(word_count):
        random_word = generate_random_word(filename)
        random_number = random.randint(1000, 9999)
        while random_word in used_words:
            random_word = generate_random_word(filename)
        used_words[i] = random_word
        print("   \033[37m\033[1m",random_word+"\033[36m"+str(random_number),"\033[0m")
    print(" ")
    input("Press Enter to regen...")

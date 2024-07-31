
class Wordlist:

     # Default word list
    wordlist = [
        "Apple", "Banana", "Mango", "Papaya", "Peach", "Orange",
        "Grape", "Kiwi", "Lemon", "Melon", "Pineapple", "Plum",
        "Cherry", "Apricot", "Avocado", "Coconut", "Date", "Pomegranate",
        "Guava", "Lychee", "Nectarine", "Olive", "Pear", "Raspberry",
        "Strawberry"
    ]

    def __init__(self, config):
        self.config = config
        wordlist = self.read_file()
        if self.check_wordlist_compliance(wordlist):
            # Wordlist is good
            self.wordlist = wordlist
        elif self.config.value['keyphrases']+self.config.value['word_amount'] >= len(self.wordlist):
            # checks if the config will work with the default wordlist, this stops hangs if its not big enough.
            print("[ \033[31mERROR\033[0m ] The default wordlist is incompatible with provided config!")
            print("[ \033[33mWARN\033[0m ] Falling back to default values. This may be undesired.")
            self.config.load_default_config()
            

     # reads in wordlist from file
    def read_file(self):
        try:
            with open(self.config.value['filename'], 'r') as file:
                words = file.readlines()
            return words
        except:
            if self.config.value['wordlist_required']:
                input("[ \033[31m\033[1mFATAL\033[0m ] A wordlist is required on this machine!")
                exit()
            else:
                print("[ \033[33mWARN\033[0m ] You are using the default wordlist, this list is publicly known and is insecure.")
                return self.wordlist

     # Writes current wordlist, currently unused
    def save_file(self):
        try:
            with open(self.config.value['filename'], 'w') as file:
                for word in self.wordlist:
                    file.write(word+"\n")
        except:
            print("[ \033[31mERROR\033[0m ] Failed to save wordlist!")

     # Return if wordlist is complaint
    def check_wordlist_compliance(self, wordlist):
        # Used to store at least keyphrases+1 unique words
        compliant_words = ["0"]*int(self.config.value['keyphrases']+self.config.value['word_amount'])
        # Loops though the word list until it finds enough unique words
        count=0
        for word in wordlist:
            if word not in compliant_words:
                compliant_words[count] = wordlist[count]
                count=count+1
            if count is self.config.value['keyphrases']+self.config.value['word_amount']:
                break
        # if count is not equal to keyphrases+1 then we looped the entire array without finding enough unique words
        if count is not self.config.value['keyphrases']+self.config.value['word_amount']:
            print("[ \033[31mERROR\033[0m ] The provided wordlist is too short and cannot be used with the current config values!")
            if self.config.value['wordlist_required']:
                input("[ \033[31m\033[1mFATAL\033[0m ] A wordlist is required on this machine!")
                exit()
            else:
                print("[ \033[33mWARN\033[0m ] Falling back to default wordlist, this list is publicly known and is insecure.")
                return False
        return True


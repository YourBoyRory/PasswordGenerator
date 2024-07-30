import configparser

class Config:

    parser = configparser.ConfigParser()

     # default values
    value = {
        'keyphrases': 5,             # amount of keyphrases to generate every time the user regens
        'number_mask': '0000',       # Mask for the number generated. "0000" - 4 didgets 0-9, "1000" first diget is 1-9 last 3 are 0-9
        'sufix_selection': ' ',      # Selects a random char from this string to sufix the keyphrase, use this if you need a special character "!@#$^&".

        'filename': 'words.txt',     # allowed word list file directory
        'wordlist_required': False,  # Do not use the default wordlist
        'word_amount': 1,            # amount of words to be selected from the allowed word list
        'word_divider': '',          # divider that seperates each word in the keyphrase
    }

    def __init__(self):
        self.read_config()


     # Reads in the config or sets the config to the default values
     # this method is a mess please dont look at it
    def read_config(self):
        try:
             # loads config values
            self.parser['General'] = { }
            self.parser['Wordlist'] = { }
            self.parser.read('config.ini')

             # General values
            self.value['keyphrases'] = self.parser['General'].getint('keyphrases', self.value['keyphrases'])
            self.value['number_mask'] = self.parser['General'].get('number_mask', self.value['number_mask'])
            self.value['sufix_selection'] = self.parser['General'].get('sufix_selection', self.value['sufix_selection'])
            # if the sufix is empty then Random will crash attempting to pick nothing, this makes sure the string is never empty
            # using white space char effectivly does the same thing as a empty string
            if self.value['sufix_selection'] == "":
                self.value['sufix_selection'] = " "

             # wordlist values values
            self.value['filename'] = self.parser['Wordlist'].get('filename', self.value['filename'])
            self.value['wordlist_required'] = self.parser['Wordlist'].getboolean('wordlist_required', self.value['wordlist_required'])
            self.value['word_amount'] = self.parser['Wordlist'].getint('word_amount', self.value['word_amount'])
            self.value['word_divider'] = self.parser['Wordlist'].get('word_divider', self.value['word_divider'])
        except:
            print("[ \033[31mERROR\033[0m ] Malformed config!")

    def save_config(self):

        self.parser['General'] = {
            'keyphrases': self.value['keyphrases'],
            'number_mask': self.value['number_mask'],
            'sufix_selection': self.value['sufix_selection'],
        }
        self.parser['Wordlist'] = {
            'filename': self.value['filename'],
            'wordlist_required': self.value['wordlist_required'],
            'word_amount': self.value['word_amount'],
            'word_divider': self.value['word_divider'],
        }
        with open('config.ini', 'w') as configfile:
            self.parser.write(configfile)

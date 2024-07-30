class Config:
     # Configure for use case
    keyphrases=5               # amount of keyphrases to generate every time the user regens: 5
    number_mask="0"*2          # Mask for the number generated. "0"*4 - 4 didgets 0-9, "1000" first diget is 1-9 last 3 are 0-9: "0"*4
    filename ="words.txt"      # allowed word list file directory: words.txt
    word_amount=1              # amount of words to be selected from the allowed word list: 1
    word_divider=""            # divider that seperates each word in the keyphrase: ""
    sufix_selection="!@#$%^&"  # Selects a random char from this string to sufix the keyphrase, use this if you need a special character "!@#$%^&".: " "
    wordlist_required=False     # Do not use the default wordlist

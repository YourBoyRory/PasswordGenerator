### Simple yet configurable script that generates random passwords 

-----------------
Uses allowed words from a file and places random numbers or characters at the end.
By default, the script will generate 5 Random passwords with 4 random numbers at the end

#### Example Output ####

      [ 1 ] Avocado7072
      [ 2 ] Nectarine6299
      [ 3 ] Cherry3774
      [ 4 ] Melon6493
      [ 5 ] Strawberry2410

The number of passphrases that are generated at one time, along with the allowed wordlist, number mask, and other options can easily be changed in a config file.
For added security, it is best to use your own word list, but if no file is provided, one with 25 fruits will be used.
Examples of both the word list format and the config can be downloaded in releases

Wordlist
--------
The allowed word list is used to generate easy-to-remember and say "passphrases"
- The allowed wordlist must have +1 the number of "keyphrases" to generate; by default, this would be 6 words in the file as keyphrases are set to 5.
- If the wordlist is missing or there are not enough words for the script to generate X unique words, a default one will be used as long as wordlist_required is set to false.
- By default, the script looks for a file named word.txt in the same directory as the executable but this behavior can be changed in the config.

## Config ##
A ``config.ini`` and ``override.ini`` files can be used to customize the passwords the program generates. The configs will be checked in this order
- The system-wide ``override.ini`` uses the same formatting as the ``config.ini`` and will be used above all configs if it exists, it will be placed in ``/ProgramData/PasswordGenerator/override.ini`` on Windows or ``/etc/PasswordGenerator/override.ini`` on Linux and Mac.
- A ``config.ini`` can be placed in the same directory as the executable and will be used instead of the main user config or the system config. The ``override.ini`` will always take precedence over this config.
- The user ``config.ini`` can also be placed in ``$USERHOME/.config/PasswordGenerator/config.ini`` or ``$USERHOME/.PasswordGenerator/config.ini`` in the uses home folder on Linux, Mac, or Windows.
  These user configs will be checked before the system-wide ``config.ini`` but after the one in the same directory as the executable. The ``override.ini`` will always take precedence over these configs.
- The system-wide ``config.ini`` will be used last if it exists, it will be placed in ``/ProgramData/PasswordGenerator/config.ini`` on Windows or ``/etc/PasswordGenerator/config.ini`` on Linux and Mac. The ``override.ini`` will always take precedence over this config.
  
If the config does not exist or if a value does not exist, the script will go down the hierarchy until it finds the value in one of the configs or it will use the default value.
#### Default ``config.ini`` with documentation ####

    [General]
    	  # number of key phrases to generate every time the user regens
    	  # must be 1 less than the words in the list unless word_amount is higher than 1
    	  # Default: 5
    	keyphrases = 5
    	
    	  # Mask for the number generated. "0000" - 4 digits 0-9, "1000" first digit is 1-9 last 3 are 0-9
    	  # Default: 0000
    	number_mask = 0000
    	
    	  # Selects a random char from this string to suffix the key phrase, use this if you need a special character "!@#$^&".
    	  # supports most special characters, except '%' due to software limitations
    	  # If left empty or disabled a blank space will be appended to the password
    	  # Default: [disabled]
    	#sufix_selection =  
    
    [Wordlist]
    	  # allowed word list file directory
    	  # Default: words.txt
    	filename = words.txt
    	
    	  # Do not use the default wordlist
    	  # Default: False
    	wordlist_required = False
    	
    	  # amount of words to be selected from the allowed word list to generate multi word passwords
    	  # changes the amount of words needed in the wordlist by keyphrases + word_amount
    	  # Default: 1
    	word_amount = 1
    	
    	  # divider string that separates each word in the keyphrase
    	  # Default: [disabled]
    	#word_divider =  

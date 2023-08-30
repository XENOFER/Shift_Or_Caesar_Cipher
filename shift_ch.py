#!/usr/bin/python3

import time
from termcolor import colored

print(colored("\n[*] Chose your option only number is valid\n", 'red'))#attrs=['blink']))#, attrs=['reverse', 'blink']))
time.sleep(.50)

while True:
    print(colored('=======================================================','light_blue'))
    x = input(colored('[+] What you want 1) Encrypt or 2) Decrypt : ','green'))
    if x == '1' or x == '2':
        break
print(colored('=======================================================','light_blue'))
time.sleep(.35)
print('\n')

en_text = input(colored("[+] Enter your text : ",'yellow'))
key = int(input(colored("[+] Enter your key number : ",'yellow')))

def encode():
    
    #en_result = [] # where the output is stored as a list
    result = ''

    for i in en_text:
        if i == " ":
            result += " "
        elif i.isupper():
            # posion of every letter check
            index = ord(i) - ord("A")
            # new indexing number 
            new_index = (index + key) % 26
            # new unicode
            new_unicode = new_index + ord("A")
            # convert unicode to character
            unicodes = chr(new_unicode)
            # save the output
            result += unicodes
        
        elif i.isnumeric():
            result += i
        
        else:
            # posion of every letter
            index = ord(i) - ord("a")
            # new indexing number 
            new_index = (index + key) % 26
            # new unicode
            new_unicode = new_index + ord("a")
            unicodes = chr(new_unicode)
            result += unicodes
    #en_result.append(result)
    #decode(result)
    #print(en_result)
    
    print(colored("\n[*] Your Original text is : ",'light_green'),en_text)
    print(colored('[*] Your Encrypted output is : ','light_green'),result)

def decode():
    de_result = ''
    for i in en_text:
        #print(i,end='')
        #print('\n')
        if i == ' ':
            de_result += i
        elif i.isupper():
            index = ord(i) - ord('A')
            new_index = (index - key) % 26
            new_unicode = new_index + ord("A")
            unicodes = chr(new_unicode)
            de_result += unicodes
            pass
        elif i.isnumeric():
            de_result += i
            pass
        else:
            index = ord(i) - ord('a')
            new_index = (index - key) % 26
            new_unicode = new_index + ord("a")
            unicodes = chr(new_unicode)
            de_result += unicodes
            pass
    print(colored("\n[*] Your encrypted text is : ",'light_green'),en_text)
    print(colored('[*] Your decrypted output is : ','light_green'),de_result)

x = int(x)
if x == 1:
    encode()
else:
    decode()   
#encode()

#decode()
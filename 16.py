import random

set_char_l  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
set_char_2  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
set_number  = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
set_special = ['~', '!', '@', '#', '$', '%', '^', '&', '*', "?"]
set_common = ["the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his","they",
              "I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when",
              "your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other",
              "about","out","many","then","them","these","so","some","her","would","make","like","him","into","time",
              "has","look","two","more","write","go","see","number","no","way","could","people","my","than","first",
              "water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","part"]

choice = int(input("Choose the type of password\n1 - weak\n2 - strong\n"))
password = ''

if choice == 1:
    password += random.choice(set_common)
    password += random.choice(set_common)
    print(password)

# set 1 - 10% | set 2 - 20% | num - 30% | spec - 40%

# password - 10 chars
if choice == 2:
    for i in range(10):
        if len(password) < 1:
            char = random.choice(set_char_l)
            password += char
        elif len(password) < 3:
            char = random.choice(set_char_2)
            password += char
        elif len(password) < 7:
            char = random.choice(set_number)
            password += char
        elif len(password) < 10:
            char = random.choice(set_special)
            password += char

    # shuffle
    list1=[]
    list1[:0]=password
    random.shuffle(list1)
    password = ''.join(list1)
    print(password)



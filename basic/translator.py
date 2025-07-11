#all vowels become g i.e. dog becomes dgg , cat becomes cgt

word = input("Input word to translate \n")
new_word='';
for letter in word:
    if letter in "AEIOU":
        new_word += 'G';
    elif letter in "aeiou":
        new_word += 'g';
    else:
        new_word += letter;
print("The translated word = \n"+new_word)
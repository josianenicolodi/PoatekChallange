''' using methods .upper(), replace() and strip() and the function expInv to manage the variable '''


word = input('Write a word or a phrase: ').upper().replace(' ', '').strip()
expInv = word[::-1]
if word == expInv:
    print('It is Palindrome, because, {} --> {}.'.format(word, expInv))
else:
    print('Is not a Palindrome.')
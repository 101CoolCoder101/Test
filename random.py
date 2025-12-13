import random
from words import *
print('There are three modes you can choose from:')
print('1. Easy Mode: Maximum 20 guesses allowed.')
print('2. Medium Mode: Maximum 15 guesses allowed.')
print('3. Hard Mode: Maximum 10 guesses allowed.')
def funct():
    ask = input('Easy, medium or hard mode (e/m/h)? ').lower()
    if ask == 'e':
        def func():
            que = input('How much letters do you want the word to be (3,4,5,6,7,8)? ')
            if que == '3':    
                word = random.choice(wordlist3)
                guess = '***'
                for n in range(20):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(3):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '4':    
                word = random.choice(wordlist4)
                guess = '****'
                for n in range(20):
                    if word!= guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(4):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '5':    
                word = random.choice(wordlist5)
                guess = '*****'
                for n in range(20):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(5):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '6':    
                word = random.choice(wordlist6)
                guess = '******'
                for n in range(20):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(6):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '7':    
                word = random.choice(wordlist7)
                guess = '*******'
                for n in range(20):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(7):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '8':    
                word = random.choice(wordlist8)
                guess = '********'
                for n in range(20):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(8):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            else:
                print('Invalid input.')
                func()
        func()
    elif ask == 'm':
        def func():
            que = input('How much letters do you want the word to be (3,4,5,6,7,8)? ')
            if que == '3':    
                word = random.choice(wordlist3)
                guess = '***'
                for n in range(15):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(3):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '4':    
                word = random.choice(wordlist4)
                guess = '****'
                for n in range(15):
                    if word!= guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(4):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '5':    
                word = random.choice(wordlist5)
                guess = '*****'
                for n in range(15):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(5):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '6':    
                word = random.choice(wordlist6)
                guess = '******'
                for n in range(15):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(6):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '7':    
                word = random.choice(wordlist7)
                guess = '*******'
                for n in range(15):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(7):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '8':    
                word = random.choice(wordlist8)
                guess = '********'
                for n in range(15):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(8):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            else:
                print('Invalid input.')
                func()
        func()
    elif ask == 'h':
        def func():
            que = input('How much letters do you want the word to be (3,4,5,6,7,8)? ')
            if que == '3':    
                word = random.choice(wordlist3)
                guess = '***'
                for n in range(10):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(3):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '4':    
                word = random.choice(wordlist4)
                guess = '****'
                for n in range(10):
                    if word!= guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(4):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '5':    
                word = random.choice(wordlist5)
                guess = '*****'
                for n in range(10):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(5):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '6':    
                word = random.choice(wordlist6)
                guess = '******'
                for n in range(10):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(6):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '7':    
                word = random.choice(wordlist7)
                guess = '*******'
                for n in range(10):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(7):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            elif que == '8':    
                word = random.choice(wordlist8)
                guess = '********'
                for n in range(10):
                    if word!=guess:
                        print('Here is the word:', guess)
                        letter = input('Guess a letter: ').upper()
                        hasLetter = False
                        newguess = []
                        for n in range(8):
                            if(letter==word[n]):
                                newguess.append(letter)
                                hasLetter = True
                            else:
                                newguess.append(guess[n])
                        guess="".join(newguess)
                        if (hasLetter==True):
                            print("Good guess; you're right!")
                        else:
                            print("Wrong! That letter isn't in the word. Try again!")
                print('The word was', word)
            else:
                print('Invalid input.')
                func()
        func()
    else:
        print('Invalid input.')
        funct()
funct()

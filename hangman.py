# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 20:15:42 2021

@author: User
"""
import random
from thewords import myword


def the_word():
    word=random.choice(myword)
    return word.upper()


def the_game(word):
    word_completed= "_" * len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    attempts=6
    print('let have some fun')
    print(the_hangman(attempts))
    print(word_completed)
    print('\n')
    while not guessed and attempts > 0:
        guess_it=input('please guess a letter or word:').upper()
        if len(guess_it) == 1 and guess_it.isalpha():
            if guess_it in guessed_letters:
                print('you already guessed it',guess_it)
            elif guess_it not in word:
                print(guess_it,'it is not in the word')
                attempts -=1
                guessed_letters.append(guess_it)
            else:
                print('nice job,',guess_it)
                guessed_letters.append(guess_it)
                word_to_list=list(word_completed)
                indice=[i for i, letter in enumerate(word) if letter == guess_it]
                for index in indice:
                    word_to_list[index] = guess_it
                word_completed=''.join(word_to_list)
                if '_'  not in word_completed:
                    guessed=True
        elif len(guess_it)==len(word) and guess_it.isalpha():
            if guess_it in guessed_words:
                print('you did that',guess_it)
            elif guess_it !=word:
                print(guess_it,'too bad that is not the word')
                attempts -=1
                guessed_words.append(guess_it)
            else:
                guessed= True
                word_completed=word
        else:
            print('you guessed it wrong')
            
        print(the_hangman(attempts))
        print(word_completed)
        print('\n')
    if guessed:
        print('congratulation')
    else:
        print('better luck next time.This is the word ' + word + '.Toodles')
              
              
              
              
              
def the_hangman(attempts):
    stages=[
                """
                    +-------+
                    +       |
                    +       o
                    +     \\|/
                    +      |
                    +     / |\
                    -
                """,
                
                """
                    +-------+
                    +       |
                    +       o
                    +      \\|/
                    +       |
                    +      /
                    -
                """,
                """
                    +-------+
                    +       |
                    +       o
                    +      \\|/
                    +       |
                    +
                    -
                """,
                """
                    +-------+
                    +       |
                    +       o
                    +      \\|
                    +       |
                    +       
                    -
                """,
                """
                    +-------+
                    +       |
                    +       o
                    +       |
                    +       |
                    +
                    -
                """,
                """
                    +-------+
                    +       |
                    +       o
                    +       
                    +
                    +
                    -
                """,
                """
                    +-------+
                    +       |
                    +
                    +
                    +
                    +
                    -
                """,
        ]
    return stages[attempts]
        

def main():
    word=the_word()
    the_game(word)
    while input('play again? (Y/N)').upper() == 'Y':
        word=the_word()
        the_game(word)
        
if __name__ == "__main__":
    main()
        
        
         
                
                   
                
                
                    
                
                
        
                    
            
               
    
    
                
             
            
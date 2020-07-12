# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:52:05 2020

@author: Jonatan

O'Reilly course "Python Fundamentals": Top 100 words scenario
"""

import re

def user_input():
    """Asks the user for the path to the textfile and checks if it exists."""
    textfile = input("Enter the path to the textfile: ")
    import os.path
    if os.path.isfile(textfile):
        return textfile
    else:
        print("Error: did not find the file you entered.")
        print("Please retry.")
        user_input()


def words_in_book(filename):
    """Takes a readable textfile as argument and returns the list of words."""
    with open(filename,"r") as f:
        try:
            text = f.read()
        except UnicodeDecodeError:
            text = open(filename, "r", encoding = "utf8").read()
    
    return re.findall(r"[a-zA-Z]+", text)

def filter_words(word_list, title = False):
    """Takes a list of words as argument and an optional bool agrument,
    removes the most common english words from the list,
    if bool argument is set to True, only title words are returned."""
    
    # 1000 common english words, obtained from https://gist.github.com/deekayen/4148741
    with open("1000words.txt","r") as g:
        common_words = g.read()

    common_words = re.findall(r"[a-zA-Z]+", common_words) # Used this to get rid of \n
    
    not_common_words = [word for word in word_list
                        if (word not in common_words
                            and word.lower() not in common_words)]
    if title:
        return [word for word in not_common_words
                if (word.istitle()
                    and not word.isupper())]
    else:
        return not_common_words
    
def create_sorted_dictionary(word_list):
    """Creates a dictionary sorted by descending value from a list of words:
        with unique words as the key 
        and the count of occurrences of that word in the list as value."""
    import collections
    dicti = dict(collections.Counter(word_list))
    return {k: v for k, v in sorted(
                                    dicti.items(), 
                                              key=lambda item: item[1], 
                                              reverse = True)}

def print_top_words(dicti, counts = 100):
    """Takes an ordered dictionary of word occurrence as argument 
    and an optional counts argument,
    returns the top counts of words in the dictionary."""
    
    
    top_words= list(dicti.keys())[:counts]

    for i in range(counts):
        key = top_words[i]
        print(i+1, key, ":", dicti[key])
    




def main():
    textfile = user_input()
    words = words_in_book(textfile)
    filterd_words = filter_words(words, True)
    dicti = create_sorted_dictionary(filterd_words)
    print_top_words(dicti)
    
    
    
main()
# Tested with "Moby Dick; or, the whale" by Herman Melville, obtained from 'gutenberg.org'
# And with "Harry Potter: The Philosopher's Stone" by J.K. Rowling, obtained from https://github.com/formcept/whiteboard/blob/master/nbviewer/notebooks/data/harrypotter/Book%201%20-%20The%20Philosopher's%20Stone.txt       
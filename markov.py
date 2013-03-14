#!/usr/bin/env python

import sys
from random import randint

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""    

    markov_chains_dict = {}

    # To do: strip out cruft later

    # break up input string of text into a list of individual words
    word_list = corpus.split() 

    # loop through list of words by index, set a tuple as a new key in the dictionary and the third word as the value. End before the last two words in the list.
    for i in range(len(word_list)-2):

        bigram = word_list[i], word_list[i+1]
        value = word_list[i+2]

        # To do: is there any way to shorten this using the get method for dicts?
        
        # if word pair doesn't already exist in the dictionary, add it as a new key and give it the third word as the value in a *list* 
        if bigram not in markov_chains_dict:
            markov_chains_dict[bigram] = [value]

        # if word pair is already in the dictionary (not unique), then append the third word to existing list of values
        else:
            markov_chains_dict[bigram].append(value)

    return markov_chains_dict

def make_text(chains, max_length):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    # add all keys from chains dict to new list
    convert_dict_list = []
    for keys in chains:
        convert_dict_list.append(keys)

    # generate a random index number to pick out a tuple from the convert_dict_list
    rand_index = randint(0, len(convert_dict_list)-1)

    # add the first and second items in that tuple as separate items to the convert_dict_list
    random_text_list = [convert_dict_list[rand_index][0], convert_dict_list[rand_index][1]]
    
    # grabs the last two items of the random_text list 
    last_two = random_text_list[-2],random_text_list[-1]
 
    while last_two in chains and len(random_text_list) < max_length:
        # values are stored in a list, generates a random index number to randomly grab value 
        rand_index = randint(0, len(chains[last_two])-1)

        # append value of key matching previous last two words from random_text_list to the list 
        random_text_list.append(chains[last_two][rand_index])
        
        # we've changed the contents of the list, reset last_two variable to be the new last two items in the last
        last_two = random_text_list[-2],random_text_list[-1]

    final_string = ' '.join(random_text_list)

    return final_string

def main():
    args = sys.argv

    # args is a tuple of what's inputted in terminal after python command, therefore can get filename using args[1]
    input_text = open(args[1]).read()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict, int(args[2]))
    print random_text

if __name__ == "__main__":
    main()
#!/usr/bin/env python

import sys
import random

def make_chains(corpus, ngram_size):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""    

    # To do: strip out cruft later

    # break up input string of text into a list of individual words
    word_list = corpus.split() 

    # this is the first ngram that will become a key in the dictionary.
    # getting a slice of the word_list from the beg of the list, with the max size passed into this func at ngram_size; converted to a tuple for use as a key in the dict
    n_gram = tuple(word_list[:ngram_size])
    
    # delete set of words being used as the first key (n_gram)
    del word_list[:ngram_size]

    markov_chains_dict = {}

    # while word_list still exists and has words in it
    while word_list:
        # taking the first word off the rest of the list
        word = word_list.pop(0)
        # looks for key in the dict, if it exists, then append word to existing list of values; if key is not in dict, set it in the dictionary with an empty list as the value, then add word to that empty list
        markov_chains_dict.setdefault(n_gram,[]).append(word)
        # set new n_gram key based on previous n_gram, starting from the 2nd item to the end of the previous n_gram, and tack on the just added word as part of the tuple
        n_gram = n_gram[1:] + (word,)

    return markov_chains_dict

def make_text(chains, max_length):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    # grab a random key from the chains dict, this is a tuple. Could be last set of words in the text??? Doesn't seem right.
    seed = random.choice(chains.keys())

    # convert the tuple into a list and add it to the list random_text_list
    random_text_list = []
    random_text_list += list(seed)

    # while the random_text_list is not yet the max length specified...
    while len(random_text_list) < max_length:
        # to deal with if the key chosen is the last set
        choices = None
        while not choices:
            choices = chains.get(seed)
            if not choices:
                seed = random.choice(chains.keys())
                random_text_list += list(seed)

        # choose a random value from the list of values in the dictionary for the seed key
        next = random.choice(chains[seed])
        # append that new value (word) to the random_text_list
        random_text_list.append(next)
        # set new seed key based on previous seed, starting from the 2nd item to the end of the previous seed, and tack on the just added next word as part of the tuple
        seed = seed[1:] + (next,)

    final_string = ' '.join(random_text_list)

    return final_string

def main():
    script, filename, ngram_size, max_length = sys.argv

    # args is a tuple of what's inputted in terminal after python command, therefore can get filename using args[1]
    input_text = open(filename).read()

    chain_dict = make_chains(input_text, int(ngram_size))
    random_text = make_text(chain_dict, int(max_length))
    print random_text

if __name__ == "__main__":
    main()
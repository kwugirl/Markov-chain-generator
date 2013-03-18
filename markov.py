#!/usr/bin/env python
import sys
import random
import twitter


mytwitteraccount = twitter.Api(consumer_key="hhMMCNyExowTD1aIuthDAQ", 
                                consumer_secret="8Wrjm9QGsgl7yeu1WzeE5MvDwTuHPsBgKSHjok9oM", 
                                access_token_key="1278575833-6po7q7qgb1qM6QJpM2ptTVhDBfwkUCqqSFJvOgR", 
                                access_token_secret="mA6Nzv6Jeun6SmbfY31QkP9e9AyYDdCuCn4Gd8rFBU")

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
    
    # grab a random key from the chains dict, this is a tuple. Could be the last key added to the dictionary, which would end the random_text_list before it reach the specified max_length
    seed = random.choice(chains.keys())

    # convert the tuple into a list and add it to the list random_text_list
    random_text_list = []
    random_text_list += list(seed)

    text_string = ' '.join(random_text_list)

    # while the random_text_list is not yet the max length specified...
    while len(text_string) < max_length: 
        # to deal with if the key chosen is the last set, because then the value would be the last word in the text and likely can't be used to make a new key. If attempted new key is the last two words & has no value, choose a random new key to restart instead.
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

        text_string = ' '.join(random_text_list)
        # print "length of text_string in while loop", len(text_string)

    # this is to strip off the last few words (usually just the last word, but might be last few words in the txt file if the last key added was the choices key)
    while len(text_string) > max_length:
        last_word = random_text_list.pop()
        text_string = text_string.rstrip(last_word)
        text_string = text_string.rstrip(" ")
        # print "inside the stripping while loop"
    
    print "length of final text_string is", len(text_string)

    return text_string

def main():
    script, filename, ngram_size, max_length = sys.argv

    # args is a tuple of what's inputted in terminal after python command, therefore can get filename using args[1]
    input_text = open(filename).read()

    chain_dict = make_chains(input_text, int(ngram_size))
    random_text = make_text(chain_dict, int(max_length))
    print random_text

    # posts to Twitter account
    #status = mytwitteraccount.PostUpdates(random_text)

if __name__ == "__main__":
    main()
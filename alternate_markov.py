def markov(corpus, ngram_size):
	words = corpus.split()
	n_gram = tuple(words[:ngram_size])
	del corpus[:ngram_size]
	d = {}
	while words:
		word = words.pop(0)
		d.setdefault(n_gram, []).append(word)
		n_gram = n_gram[1:] + (word,)
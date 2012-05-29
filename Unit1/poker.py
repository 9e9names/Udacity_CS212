def poker(hands):
	#Return the best hand: poker([hand,...]) => hand
	return max(hands, key = hand_rank)

def hand_rank(hand):
	#Return a value indicating the ranking of a hand
	ranks = card_ranks(hand)
	if straight(ranks) and flush(hand):
		return (8, max(ranks))
	elif kind(4, ranks):
		return (7, kind(4, ranks), kind(1, ranks))
	elif kind(3, ranks) and kind(2, ranks):
		return (6, kind(3, ranks), kind(2, ranks))
	elif flush(hand):
		return (5, (ranks))
	elif straight(ranks):
		return (4, max(ranks))
	elif kind(3, ranks):
		return (3, (ranks))
	elif two_pair(ranks):
		return (2. (ranks))
	elif kind(2, ranks):
		return (1, (ranks))
	else:
		return (0, (ranks))

def test():
	#Test cases for function in poker program
	sf = "6C 7C 8C 9C TC".split()
	fk = "9D 9H 9S 9C 7D".split()
	fh = "TD TC TH 7C 7D".split()
	assert poker([sf, fk, fh]) == sf
	assert poker(fk, fh) == fk
	assert poker(fh, fh) == fh
	assert poker([fh]) == fh
	assert poker([fk] + 99*[fh]) == fk
	assert hand_rank(sf) == (8, 10)
	assert hand_rank(fk) == (7, 9, 7)
	assert hand_rank(fh) == (6, 10, 7)
	return "test_pass"

print test()
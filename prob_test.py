def prob_a_or_b(a, b, all_possible_outcomes):
    # probability of event a
    prob_a = len(a)/len(all_possible_outcomes)
    print(prob_a)
	
	# probability of event b
    prob_b = len(b)/len(all_possible_outcomes)
    print(prob_b)
	# intersection of events a and b
    inter = a.intersection(b)
	
	# probability of intersection of events a and b
    prob_inter = len(inter)/len(all_possible_outcomes)
    print(prob_inter)
	
	# add return statement here
    return (prob_a + prob_b) - prob_inter 

# rolling a die once and getting an even number or an odd number
evens = {2, 4, 6}
odds = {1, 3, 5}
die = {1, 2, 3, 4, 5, 6}

print(prob_a_or_b(evens, odds, die))



def max_liste(liste):
	for obj in liste:
		assert type(obj) is (int or float), "Your list should only contain float or int values!"
		
			 
	return max(liste)

def absolute(val):
	assert type(val) is (int or float), "Your value is NaN!"
	return abs(val)

if __name__ == '__main__':
	print(max_liste([1,2,3,4,9,]))
	print(absolute(-5))



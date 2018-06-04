
def average(liste):
	sum=0
	assert type(liste) = list , "your given object is not a list"
	assert len(liste) > 0, "List is emtpy"

	for item in liste:
		assert type(item) is (int or float), "something is NaN"
		
		sum+=item

	return (sum/len(liste))

def median(liste):
        assert type(liste) = list , "your given object is not a list"
	assert len(liste) > 0, "List is emtpy"
	sorted_list = sorted(liste)
	if len(liste)%2 == 1:
		return sorted_list[int(len(sorted_list)/2)]
	else:
		return ((sorted_list[int(len(sorted_list)/2)]+sorted_list[int(len(sorted_list)/2-1)])/2.0)

if __name__ == '__main__':
	
	print(average([1,2,3,4,5,])) 
	print(median([1,3,5,7,9,10]))

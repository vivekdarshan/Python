#date, name, price = ['December 23, 2015', 'Bread Gloves', 8.51]
#print(name)

#This is Python 3 concept does not work in Python 2
def drop_first_last(grades):
	first, *middle, last = grades
	avg = sum(middle) / len(middle)
	print(avg)

drop_first_last([65, 76, 98, 54, 21])
drop_first_last([65, 76, 98, 54, 21, 54, 65, 99, 88, 78])
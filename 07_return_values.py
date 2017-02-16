def allowed_dating_age(my_age):
	girls_age = my_age/2 + 7
	return girls_age

vivek_limit = allowed_dating_age(27)
akash_limit = allowed_dating_age(22)
print "Vivek can date girls", vivek_limit, "or older"
print "Akash can date girls", akash_limit, "or older"
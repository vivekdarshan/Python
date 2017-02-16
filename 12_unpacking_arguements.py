def health_calculator(age, apples_ate, cigs_smoked):
	answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
	print answer

vivek_data = [27, 28, 0]

health_calculator(vivek_data[0], vivek_data[1], vivek_data[2])
health_calculator(*vivek_data)
def check_monthnum(monthname1): 
	""" 
	Write a function to check whether the given month name contains 28 days or not. 
	""" 
	month_days = {
		"January": 31,
		"February": 28,
		"March": 31,
		"April": 30,
		"May": 31,
		"June": 30,
		"July": 31,
		"August": 31,
		"September": 30,
		"October": 31,
		"November": 30,
		"December": 31
	}
	return month_days.get(monthname1, 0) == 28
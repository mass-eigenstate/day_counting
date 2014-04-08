from datetime import date

months        = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
fiscal_months = ('oct', 'nov', 'dec', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep')
days_month    = {'jan':31, 'feb':28, 'mar':31, 'apr':30, 'may':31, 'jun':30, 
                 'jul':31, 'aug':31, 'sep':30, 'oct':31, 'nov':30, 'dec':31 }

def leap_year (year):
	if (year % 4 == 0):
		# Can be a leap year
		if (year % 400 == 0):
			return True
		else:
			if (year % 100 == 0):
				return False
			else:
				return True
	else:
		# Not a leap year
		return False

def day_of_year (date1=date.today()):
	days = 0
	if (leap_year(date1.year)):
		days_month['feb'] = 29
	dmonth = months[date1.month-1] #months tuple is zero based index; date uses 1-12 for months
	for mon in months:
		if (mon == dmonth):
			# Reached the month of the date just add the day in the date and break out of the loop
			days = days + date1.day
			break
		else:
			# Just add the days in the month
			days = days +  days_month[mon]
	days_month['feb'] = 28     #Put the number of days back to 28
	return days

def day_of_fiscalyear (date1=date.today()):
	## Input is a date in regular years
	days = 0
	if (leap_year(date1.year)):		
		days_month['feb'] = 29
	dmonth = months[date1.month-1]
	for mon in fiscal_months:
		if (mon == dmonth):
			# Reached the month of the date just add the day in the date and break out of the loop
			days = days + date1.day
			break
		else:
			# Just add the days in the month
			days = days +  days_month[mon]
	days_month['feb'] = 28     #Put the number of days back to 28
	return days

def days_between_dates (date1, date2):

	if (date1.year == date2.year):
		# Both dates are in the same year
		return abs(day_of_year(date1)-day_of_year(date2))
	else:
		days = 0
		if (date1.year < date2.year):		#date 1 is earlier
			year1=date1.year
			year2=date2.year
			if (leap_year(date1.year)):
				days += 1 					#There is an extra day in the yeap year
			days += 365-day_of_year(date1)	#First year remaining days in the year
			days += day_of_year(date2)		#Last year the number of days so far

		else:								#date2 is earlier
			year1=date2.year
			year2=date1.year
			if (leap_year(date2.year)):
				days += 1 					#There is an extra day in the yeap year
			days += 365-day_of_year(date2)	#First year remaining days in the year
			days += day_of_year(date1)		#Last year the number of days so far
		#
		# Loop over the years between year1 and year2. Add 365 days for regular years and 366 
		# for leap years.
		#
		y = year1+1
		while (y < year2):
			if (leap_year(y)):
				days += 366
			else:
				days += 365
			y += 1

		return days

print "1200 is a leap year", leap_year(1200)
print "1900 is a leap year", leap_year(1900)
print "1963 is a leap year", leap_year(1963)
print "1984 is a leap year", leap_year(1984)

print "January 1, 2000 is day ",   day_of_year(date(2000,1,1))
print "March 1, 1999 is day ",     day_of_year(date(1999,3,1))
print "March 1, 2000 is day ",     day_of_year(date(2000,3,1))
print "December 30, 1999 is day ", day_of_year(date(1999,12,30))
print "December 30, 2000 is day ", day_of_year(date(2000,12,30))
print "December 31, 2001 is day ", day_of_year(date(2001,12,31))

print "December 31, 2001 is day ", day_of_fiscalyear(date(2001,12,31)), "of the fiscal year"
print "October, 1 2001 is day ",   day_of_fiscalyear(date(2001,10,1)), "of the fiscal year"
print "March 1, 2004 is day ",     day_of_fiscalyear(date(2004,3,1)), "of the fiscal year"
print "March 1, 2005 is day ",     day_of_fiscalyear(date(2005,3,1)), "of the fiscal year"

print "Days between January 1, 2000 and March 1, 2000 is", days_between_dates(date(2000,1,1),
	                                                                       date(2000,3,1))
print "Days between January 1, 2001 and March 1, 2001 is", days_between_dates(date(2001,1,1),
	                                                                       date(2001,3,1))
print "Days between January 1, 2000 and March 1, 2001 is", days_between_dates(date(2000,1,1),
	                                                                       date(2001,3,1))
print "Days between January 1, 2000 and March 1, 2001 is", days_between_dates(date(2001,3,1),
	                                                                       date(2000,1,1))

print "Days between January 1, 2000 and January 1, 2010 is", days_between_dates(date(2010,1,1),
	                                                                       date(2000,1,1))
print "Today is day number", day_of_year(), "of the year"
print "Today is day number", day_of_fiscalyear(), "of the fiscal year"

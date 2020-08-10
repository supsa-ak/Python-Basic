import datetime
import pytz

#get todays date
#today = datetime.date.today()
#print(today)



#birthday = datetime.date(2002 , 3 , 13)
#print(birthday)



#days_since_birthday = today - birthday
#print(days_since_birthday)

#days_since_birthday = (today - birthday).days
#print(days_since_birthday)

#subtracting days
#tdelta = datetime.timedelta(days = 10)
#print(today - tdelta)

#tdelta = datetime.timedelta(days = 10)
#print(today + tdelta)

#print(today.day)
#print(today.weekday())




#print(datetime.time(9,18,30,18))

#print(datetime.datetime.today())

#datetime.date y-m-d
#datetime.time h-m-s-microsec
#datetime.datetime y-m-d-h-m-s-microsec

#Gives Error
#print(datetime.time.now())

#subtracting hours
#print(datetime.datetime.now())

#hour_delta = datetime.timedelta(hours=10)
#print(datetime.datetime.now()+hour_delta)



datetime_today = datetime.datetime.now(tz=pytz.UTC)
print(datetime_today)

#datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
#print(datetime_pacific)


#for t in pytz.all_timezones:
 # print(t)


datetime_indian = datetime_today.astimezone(pytz.timezone('Asia/Kolkata'))
print(datetime_indian)



#string formatting with dates



#2020-5-26 -> May 5,2020
#strftime (f=formatting)
print(datetime_indian.strftime('%B %d ,%Y'))

#May 5,2020  -> 2020-5-26
#strptime (p=parsing)
print(datetime.datetime.strptime('May 26,2020','%B %d,%Y'))

#This gives object
print(repr(datetime.datetime.strptime('May 26,2020','%B %d,%Y')))


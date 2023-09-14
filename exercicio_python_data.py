#make a time and date setting 
from datetime import datetime, timedelta

#date object now 
now = datetime.now()
print(now)

#add five_days now 
five_days = timedelta(days = 5) 

#add five_days now

future_date = five_days + now

print(future_date)




















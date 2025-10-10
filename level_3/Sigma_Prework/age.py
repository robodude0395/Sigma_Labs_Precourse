import datetime
from get_param_lib import get_parameter

current_time = datetime.datetime.now()

valid_months = [str(i) for i in range(1, 13)]
valid_days = [str(i) for i in range(1, 32)]

def return_datetime_diff(date1 : datetime.datetime, date2 : datetime.datetime):
    diff = abs((date1 - date2).days)
    years = diff//365
    months = (diff-(years*365))//31
    days = (diff-(years*365)-(months*31))
    return (years, months, days)


#-----MAIN PROGRAM-----
year = get_parameter("Enter year: ", int)
month = get_parameter("Enter month: ", int, valid_months)
day = get_parameter("Enter day: ", int, valid_days)

user_time = datetime.datetime(year, month, day)

years = return_datetime_diff(current_time, user_time)[0]

print(f"{years} years difference between this date and now")

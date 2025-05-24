def add_time(start, duration, starting_day=None):

    days_of_week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

    #start
    is_pm = False
    if start.endswith(" PM"): is_pm = True
    start_hours, start_minutes = map(int, start[:-3].split(':')) 
    if is_pm: start_hours +=  12
    start_total_time = start_hours * 60 + start_minutes

    #duration
    duration_hours, duration_minutes = map(int, duration.split(':'))

    if duration_minutes < 60:
        duration_total_time = duration_hours * 60 + duration_minutes

        total_time = start_total_time + duration_total_time
        
        #I calculate how many days I will move forward in days_of_week
        days_passed = total_time // 1440 #1440 is the number of minutes in one full day  integer division
        remaining_minutes = total_time % 1440 #remainder of the division

        #New time
        new_hours = remaining_minutes // 60
        new_minutes = remaining_minutes % 60

        #calculate display hour and period
        if new_hours == 0: 
            #new_hours == 0 happens when remaining_minutes is between 0 and 59 (because less than 60 minutes means 0 complete hours)
            display_hour = 12
            period = "AM"
        elif new_hours < 12:
            display_hour = new_hours
            period = "AM"
        elif new_hours == 12:
            display_hour = 12
            period = "PM"
        else:
            display_hour = new_hours - 12 #converts a 24-hour format time into a 12-hour format
            period = "PM" 

        #I update the day
        if starting_day:
            if starting_day.lower() in days_of_week:
                starting_day_index = days_of_week.index(starting_day.lower())
                new_day_index = (starting_day_index + days_passed) % 7
                #example: (4 + 3) % 7 = 0 → monday
                #(4 + 1) % 7 = 5 -> saturday
                new_day = days_of_week[new_day_index].capitalize()
        else:
            new_day = None

        new_time = f"{display_hour}:{new_minutes:02} {period}"
        if new_day: new_time += f", {new_day}"
        if days_passed == 1: new_time += " (next day)"
        elif days_passed > 1: new_time += f" ({days_passed} days later)"

    return new_time

print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('11:43 AM', '00:20'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 PM', '24:20', 'tueSday'))
print(add_time('6:30 PM', '205:12'))
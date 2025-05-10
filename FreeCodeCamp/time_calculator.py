def add_time(start, duration, starting_day=None):

    days_of_week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

    #if duration.count(':') == 1 and duration[0: duration.indexOf(':')].isdigit() and int(duration[duration.indexOf(':') + 1:]) < 60:

    if start[-2:] in ("AM", "PM") and int(start[:2]) in range(0, 13) and duration.count(':') == 1:
        hours, minutes = duration.split(':')
        if hours.isdigit() and minutes.isdigit() and int(minutes) < 60:
            if starting_day.lower in days_of_week:
                pass
                #-> si new_time es un nuevo día:
                #print(f"{new_time} (next day)")

                #-> si new_time es mayor a un día:
                #print(f"{new_time} (n days later)")

    #-> starting_day -> días de la semana -> tupla inmutable, case insensitive


    new_time =  start + duration

    return new_time
def add_time(start, duration, starting_day=None):

    days_of_week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

    #start
    pm = False
    if (start[-2:] in ("AM", "PM") and start.count(':') == 1): #Chequea si termina en buen formato
        if start.endswith(" PM"): #Chequeo para reformatear en el futuro
            pm = True
        start_hours, start_minutes = map(int, start[:-3].split(':')) #quita el formato y divide
        if start_hours in range(0, 13) and start_minutes < 60: 
            if pm: 
                start_hours +=  12 #formatea a 24hs
            start_total_time = start_hours * 60 + start_minutes

            #duration
            if duration.count(':') == 1:
                duration_hours, duration_minutes = map(int, duration.split(':'))
                if duration_minutes < 60:
                    duration_total_time = duration_hours * 60 + duration_minutes
                    total_time = start_total_time + duration_total_time
                    
                    # Días pasados
                    days_passed = total_time // 1440 #1440 minutos en un día
                    remaining_minutes = total_time % 1440 #horas

                    # Horario final
                    new_hours = remaining_minutes // 60
                    new_minutes = remaining_minutes % 60

                    if new_hours == 0:
                        display_hour = 12
                        period = "AM"
                    elif new_hours < 12:
                        display_hour = new_hours
                        period = "AM"
                    elif new_hours == 12:
                        display_hour = 12
                        period = "PM"
                    else:
                        display_hour = new_hours - 12
                        period = "PM"

                    # Día de la semana final
                    if starting_day:
                        if starting_day.lower() in days_of_week:
                            starting_day_index = days_of_week.index(starting_day.lower())
                            new_day_index = (starting_day_index + days_passed) % 7
                            new_day = days_of_week[new_day_index].capitalize()
                        else:
                            return "Error: día inválido."
                    else:
                        new_day = None

                    # Armado del string final
                    new_time = f"{display_hour}:{new_minutes:02} {period}"
                    if new_day:
                        new_time += f", {new_day}"
                    if days_passed == 1:
                        new_time += " (next day)"
                    elif days_passed > 1:
                        new_time += f" ({days_passed} days later)"

                else:
                    print("Los minutos no pueden ser iguales o mayores a 60")
            else:
                print("Horas y minutos deben estar separados por :")
        else:
            print("El formato de horas minutos es de 0 a 12hs y de 0 a 59 minutos")
    else: 
        print("No termina en formato: ': AM/PM' ")

    return new_time

print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('11:43 AM', '00:20'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 PM', '24:20', 'tueSday'))
print(add_time('6:30 PM', '205:12'))





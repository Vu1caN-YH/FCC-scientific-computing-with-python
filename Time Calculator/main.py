def add_time(start, duration, day = ''):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    days_formatted = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
        ]

    # list comprehension
    times = [start, duration]
    hours = [t.split()[0].split(':')[0] for t in times]
    minutes = [t.split()[0].split(':')[1] for t in times]
    am_pm = [t.split()[1] if len(t.split()) > 1 else '' for t in times]

    start_index = 0
    duration_index = 1
    
    #convert to 24hr clock
    initial_am_pm = am_pm[start_index]
    start_hour = int(hours[start_index])
    if initial_am_pm == 'PM':
        start_hour += 12
    elif start_hour == 12 and initial_am_pm == 'AM':
        start_hour = 0
        
    #add time in 24 hr frame
    total_hour = start_hour + int(hours[duration_index])
    total_minutes = int(minutes[start_index]) + int(minutes[duration_index])
    if total_minutes >= 60:
        end_minutes = total_minutes - 60
        total_hour += 1
    else: 
        end_minutes = total_minutes
        
    #convert 24 hr frame to 12 hr frame
    end_hour = total_hour % 12
    if end_hour == 0: 
        end_hour = 12
        
    #am_pm flip
    end_hour_24 = total_hour % 24
    final_am_pm = "AM" if end_hour_24 < 12 else "PM"

    #days
    if day == '':
        num_days_increased = total_hour // 24
        cases = {
            0: '',
            1: ' (next day)',
        }
        day_shift = cases.get(num_days_increased, f" ({num_days_increased} days later)")

    else:
        num_days_increased = total_hour // 24
        final_day_index = ((days.index(day.lower()) + num_days_increased) % 7)
        final_day = days_formatted[final_day_index]
        cases = {
            0:', ' + final_day,
            1:', ' + final_day + ' (next day)',
        }
        day_shift = cases.get(num_days_increased, f", {final_day} ({num_days_increased} days later)")

    end_time = f"{end_hour}:{end_minutes:02d} {final_am_pm}{day_shift}"
    return end_time

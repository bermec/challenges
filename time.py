
now = input("Enter time in 24hr format 00:00 or 2359")
later = input("Enter minutes to add")

# extract hours, minutes
hours = now[:2]
mins = now[-2:]

# convert to integers
hours = int(hours)
mins = int(mins)

# convert added minutes to hours, minutes
later_hours = int(later)//60
later_mins = int(later) % 60

# add the minutes together
total_mins = int(mins) + later_mins

# more than one hour?
if total_mins >= 60:
    hours += 1

# final result, minutes, hours
final_mins = str(total_mins%60)
final_hours = str(hours%24 + later_hours)

# pad out with zeros
final_hours = final_hours.rjust(2, '0')
final_mins = final_mins.rjust(2, '0')

print(str(final_hours) + ':' + str(final_mins))
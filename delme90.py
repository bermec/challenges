day_accumulator = 191
this_day_number = 2


candidate_day_of_week = ((this_day_number - day_accumulator % 7) + 7) % 7
print(candidate_day_of_week)
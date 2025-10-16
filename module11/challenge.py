import datetime
current_date = datetime.datetime.now()

print("Current Date and Time:", current_date)
print("Year:", current_date.year)
print("Month:", current_date.month)
print("Day:", current_date.day)
print("Hour:", current_date.hour)
print("Minute:", current_date.minute)
print("Second:", current_date.second)
print("Microsecond:", current_date.microsecond)

print("\n--- Using timedelta ---")


future_date = current_date + datetime.timedelta(days=100)
past_date = current_date - datetime.timedelta(days=100)

print("Date 100 days in the future:", future_date)
print("Date 100 days in the past:", past_date)

print("\n--- Writing a specific date to file ---")


specific_date = datetime.datetime(2024, 9, 1, 8, 0, 0)


formatted_date = specific_date.strftime("%Y-%m-%d %H:%M:%S")


with open("formatted_dates.txt", "w") as file:
    file.write("Specific Date and Time: " + formatted_date)

print("Formatted date written to 'formatted_dates.txt' successfully!")
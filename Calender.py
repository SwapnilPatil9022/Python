import calendar

def generate_calendar(year, month):
    # Using the calendar module to generate the calendar for the given year and month
    cal = calendar.monthcalendar(year, month)
    
    # Printing the header
    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")
    
    # Printing the calendar
    for week in cal:
        for day in week:
            if day == 0:
                print("  ", end=" ")  # Print two spaces for empty days
            else:
                print(f"{day:2}", end=" ")  # Right-align the day number with 2 spaces padding
        print()  # Move to the next line for the next week

# Example usage:
year = 2024
month = 3
generate_calendar(year, month)

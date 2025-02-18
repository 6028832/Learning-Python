from datetime import datetime, timedelta
import csv

# Function to generate dates for a weekly repeating schedule
def generate_weekly_dates(start_date, end_date, day):
    current_date = start_date
    dates = []
    while current_date <= end_date:
        if current_date.strftime("%A") == day:
            dates.append(current_date)
        current_date += timedelta(days=1)
    return dates

# Reformatting the schedule for Google Calendar
start_date = datetime(2025, 1, 22)  # Example start date for repeating events
end_date = datetime(2025, 3, 22)    # Example end date for repeating events

# Original schedule details
google_calendar_schedule = [
    ["Subject", "Start Date", "Start Time", "End Date", "End Time", "Description", "Location", "All Day Event"]
]

time_mapping = {
    "07:00-07:30": ("07:00 AM", "07:30 AM"),
    "07:30-08:00": ("07:30 AM", "08:00 AM"),
    "08:00-08:30": ("08:00 AM", "08:30 AM"),
    "09:00-15:00": ("09:00 AM", "03:00 PM"),
    "15:00-15:30": ("03:00 PM", "03:30 PM"),
    "15:30-16:00": ("03:30 PM", "04:00 PM"),
    "16:00-16:30": ("04:00 PM", "04:30 PM"),
    "16:30-17:30": ("04:30 PM", "05:30 PM"),
    "17:30-18:00": ("05:30 PM", "06:00 PM"),
    "18:00-19:00": ("06:00 PM", "07:00 PM"),
    "19:00-19:30": ("07:00 PM", "07:30 PM"),
    "19:30-21:00": ("07:30 PM", "09:00 PM"),
    "21:00-21:30": ("09:00 PM", "09:30 PM"),
    "21:30-22:00": ("09:30 PM", "10:00 PM"),
    "22:00-23:00": ("10:00 PM", "11:00 PM"),
    "23:00": ("11:00 PM", "11:59 PM"),
    "05:30-06:00": ("05:30 AM", "06:00 AM"),
    "06:00-06:30": ("06:00 AM", "06:30 AM"),
    "06:30-13:00": ("06:30 AM", "01:00 PM"),
    "13:00-13:30": ("01:00 PM", "01:30 PM"),
    "13:30-14:00": ("01:30 PM", "02:00 PM"),
    "14:00-16:00": ("02:00 PM", "04:00 PM"),
    "16:00-17:00": ("04:00 PM", "05:00 PM"),
    "17:00-19:00": ("05:00 PM", "07:00 PM"),
    "19:00-21:00": ("07:00 PM", "09:00 PM"),
    "21:00-22:00": ("09:00 PM", "10:00 PM"),
    "07:00-08:00": ("07:00 AM", "08:00 AM"),
    "08:00-11:00": ("08:00 AM", "11:00 AM"),
    "11:00-12:30": ("11:00 AM", "12:30 PM"),
    "12:30-13:30": ("12:30 PM", "01:30 PM"),
    "13:30-14:00": ("01:30 PM", "02:00 PM"),
    "16:00-18:00": ("04:00 PM", "06:00 PM"),
    "18:00-19:00": ("06:00 PM", "07:00 PM")
}

# Schedule with messages to match
schedule_events = [
    ("Weekdays", "07:00-07:30", "Morning Routine: Freshen up, light stretch, hair care.", "Start the day with energy!"),
    ("Weekdays", "07:30-08:00", "Breakfast", "Fuel up for the day ahead."),
    ("Weekdays", "08:00-08:30", "Bike to School", "Stay active with your commute."),
    ("Weekdays", "09:00-15:00", "School", "Focus on learning and enjoy time with friends."),
    ("Weekdays", "15:00-15:30", "Bike Home", "A refreshing way to transition from school."),
    ("Weekdays", "15:30-16:00", "Break: Snack and limited phone use.", "Take a moment to recharge."),
    ("Weekdays", "16:00-16:30", "Exercise: Strength or cardio.", "Consistency builds strength!"),
    ("Weekdays", "16:30-17:30", "Homework/Study", "Focus using the Pomodoro Technique."),
    ("Weekdays", "17:30-18:00", "Dinner Preparation/Family Time", "Connect and share moments."),
    ("Weekdays", "18:00-19:00", "Dinner with Family", "Enjoy a hearty meal together."),
    ("Weekdays", "19:00-19:30", "Relaxation", "Take a walk or watch a video."),
    ("Weekdays", "19:30-21:00", "Hobbies/Personal Projects", "Pursue what you love."),
    ("Weekdays", "21:00-21:30", "Plan the Next Day", "Reflect and prepare for tomorrow."),
    ("Weekdays", "21:30-22:00", "Evening Hair Care", "Brush out buildup and refresh your scalp."),
    ("Weekdays", "22:00-23:00", "Relaxation", "Unwind before sleep."),
    ("Weekdays", "23:00", "Sleep", "Rest and recharge."),
    ("Saturday", "05:30-06:00", "Morning Routine: Quick freshening up, small breakfast.", "Prepare for the workday."),
    ("Saturday", "06:00-06:30", "Commute to Work", "Set the tone for a productive day."),
    ("Saturday", "06:30-13:00", "Work", "Stay focused and efficient."),
    ("Saturday", "13:00-13:30", "Lunch", "Replenish your energy."),
    ("Saturday", "13:30-14:00", "Exercise: Strength", "Quick workout to stay active."),
    ("Saturday", "14:00-16:00", "Homework/Study", "Tackle school tasks."),
    ("Saturday", "16:00-17:00", "Relaxation or Light Activity", "Unwind from work."),
    ("Saturday", "17:00-19:00", "Family Time", "Share meaningful moments."),
    ("Saturday", "19:00-21:00", "Hobbies/Personal Projects", "Enjoy personal interests."),
    ("Saturday", "21:00-22:00", "Plan the Next Week", "Organize and reflect."),
    ("Saturday", "22:00-23:00", "Relaxation and Evening Hair Care", "Brush out buildup and unwind."),
    ("Saturday", "23:00", "Sleep", "Get well-deserved rest."),
    ("Sunday", "07:00-08:00", "Morning Routine: Stretching, breakfast, hair care.", "Start Sunday refreshed."),
    ("Sunday", "08:00-11:00", "Homework/Study", "Focus on tasks requiring concentration."),
    ("Sunday", "11:00-12:30", "Family Activity or Hobby", "Enjoy quality time or explore interests."),
    ("Sunday", "12:30-13:30", "Lunch and Relaxation", "Recharge for the afternoon."),
    ("Sunday", "13:30-14:00", "Exercise: Flexibility (Yoga)", "Stretch and improve flexibility."),
    ("Sunday", "14:00-16:00", "Hobbies/Personal Projects", "Work on creative or enjoyable projects."),
    ("Sunday", "16:00-18:00", "Relaxation or Light Activity", "Take it easy or have fun."),
    ("Sunday", "18:00-19:00", "Dinner with Family", "Share a nice meal together."),
    ("Sunday", "19:00-21:00", "Unwind", "Prepare mentally for the week ahead."),
    ("Sunday", "21:00-22:00", "Plan for the Week and Evening Hair Care", "Organize and refresh."),
    ("Sunday", "22:00-23:00", "Relaxation", "Take time to relax before bed."),
    ("Sunday", "23:00", "Sleep", "Recharge for the new week.")
]

# Convert schedule to Google Calendar format
for event in schedule_events:
    days, time, subject, description = event
    start_time, end_time = time_mapping[time]
    days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] if days == "Weekdays" else [days]
    for day in days_list:
        dates = generate_weekly_dates(start_date, end_date, day)
        for date in dates:
            start_date_str = date.strftime("%m/%d/%Y")
            end_date_str = start_date_str  # Same day for all events here
            google_calendar_schedule.append([
                subject, start_date_str, start_time, end_date_str, end_time, description, "", ""
            ])

# File path for Google Calendar import
google_calendar_file_path = "Google_Schedule.csv"

# Write to CSV file
with open(google_calendar_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(google_calendar_schedule)

google_calendar_file_path

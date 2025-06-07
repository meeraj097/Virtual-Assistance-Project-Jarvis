import datetime
import time
import threading

reminders = []
tasks = []

def speak(message):
    print(message)

def parse_relative_time(time_str):
    now = datetime.datetime.now()
    time_str = time_str.lower()

    if "today" in time_str:
        time_part = time_str.split("at")[-1].strip()
        reminder_time = datetime.datetime.strptime(time_part, "%I:%M %p" if 'am' in time_part or 'pm' in time_part else "%H:%M")
        reminder_time = now.replace(hour=reminder_time.hour, minute=reminder_time.minute, second=0)
        return reminder_time
    elif "tomorrow" in time_str:
        time_part = time_str.split("at")[-1].strip()
        reminder_time = datetime.datetime.strptime(time_part, "%I:%M %p" if 'am' in time_part or 'pm' in time_part else "%H:%M")
        reminder_time = (now + datetime.timedelta(days=1)).replace(hour=reminder_time.hour, minute=reminder_time.minute, second=0)
        return reminder_time
    else:
        return datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

def add_reminder(time_str, message):
    try:
        reminder_time = parse_relative_time(time_str)
        reminders.append({"time": reminder_time, "message": message})
        speak(f"Reminder set for {reminder_time.strftime('%Y-%m-%d %H:%M:%S')}")
    except ValueError:
        speak("Incorrect date-time format. Please use 'today at HH:MM', 'tomorrow at HH:MM', or 'YYYY-MM-DD HH:MM:SS'")

def add_task_reminder(time_str, task_name):
    try:
        reminder_time = parse_relative_time(time_str)
        tasks.append({"time": reminder_time, "task_name": task_name})
        speak(f"Task reminder set for {task_name} at {reminder_time.strftime('%Y-%m-%d %H:%M:%S')}")
    except ValueError:
        speak("Incorrect date-time format. Please use 'today at HH:MM', 'tomorrow at HH:MM', or 'YYYY-MM-DD HH:MM:SS'")

def check_reminders():
    while True:
        now = datetime.datetime.now()
        for reminder in reminders[:]:
            if now >= reminder["time"]:
                speak(f"Reminder: {reminder['message']}")
                reminders.remove(reminder)
        for task in tasks[:]:
            if now >= task["time"]:
                speak(f"Task Reminder: {task['task_name']}")
                tasks.remove(task)
        time.sleep(30)  # Check every 30 seconds

threading.Thread(target=check_reminders, daemon=True).start()
#
# add_reminder("today at 18:00", "Meeting with Bob")
# add_task_reminder("tomorrow at 09:00", "Submit project report")

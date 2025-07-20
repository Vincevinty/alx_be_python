# daily_reminder.py

# 1. Prompt for a Single Task:
task_description = input("Enter a task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound_input = input("Is the task time-bound (yes/no)? ").lower()

is_time_bound = False
if time_bound_input == 'yes':
    is_time_bound = True

# 2. Process the Task Based on Priority and Time Sensitivity:
reminder_message = ""
action_required = ""

match priority:
    case 'high':
        reminder_message = f"Reminder: '{task_description}' is a HIGH priority task."
        if is_time_bound:
            action_required = "That requires immediate attention today!"
        else:
            action_required = "It's important, but not strictly time-sensitive."
    case 'medium':
        reminder_message = f"Reminder: '{task_description}' is a MEDIUM priority task."
        if is_time_bound:
            action_required = "Try to get it done today."
        else:
            action_required = "It can be done soon."
    case 'low':
        reminder_message = f"Reminder: '{task_description}' is a LOW priority task."
        if is_time_bound:
            action_required = "It would be good to get this done today if possible."
        else:
            action_required = "It can wait if other tasks are more pressing."
    case _:
        reminder_message = f"Reminder: '{task_description}' has an unrecognized priority. Please set it appropriately."
        action_required = "Review this task's priority."

# 3. Provide a Customized Reminder:
print("\n" + reminder_message)
print(action_required)
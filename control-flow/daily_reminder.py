# طلب إدخال المستخدم للمهمة
task = input("Enter your task: ")

# طلب إدخال الأولوية (high, medium, low)
priority = input("Priority (high/medium/low): ").lower()

# طلب إدخال ما إذا كانت المهمة حساسة للوقت
time_bound = input("Is it time-bound? (yes/no): ").lower()

# طباعة تذكير استنادًا إلى الأولوية وحساسية الوقت باستخدام Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# تعديل التذكير إذا كانت المهمة حساسة للوقت
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# طباعة التذكير النهائي
print(f"\nReminder: {reminder}")


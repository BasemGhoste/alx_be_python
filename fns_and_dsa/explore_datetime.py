from datetime import datetime, timedelta

# الجزء الأول: عرض التاريخ والوقت الحاليين
def display_current_datetime():
    current_date = datetime.now()  # الحصول على التاريخ والوقت الحاليين
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # تنسيق التاريخ والوقت
    print(f"Current date and time: {formatted_date}")

# الجزء الثاني: حساب التاريخ المستقبلي
def calculate_future_date(days):
    current_date = datetime.now()  # الحصول على التاريخ الحالي
    future_date = current_date + timedelta(days=days)  # حساب التاريخ المستقبلي بإضافة الأيام
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # تنسيق التاريخ
    print(f"Future date: {formatted_future_date}")

# الدالة الرئيسية
def main():
    # عرض التاريخ والوقت الحاليين
    display_current_datetime()

    # طلب عدد الأيام من المستخدم
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # حساب وعرض التاريخ المستقبلي
        calculate_future_date(days_to_add)
    except ValueError:
        print("Invalid input. Please enter a valid number of days.")

if __name__ == "__main__":
    main()

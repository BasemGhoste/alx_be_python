# تعريف العوامل العالمية لتحويل الوحدات
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# دالة لتحويل فهرنهايت إلى سيليزيوس
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# دالة لتحويل سيليزيوس إلى فهرنهايت
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# التفاعل مع المستخدم
def main():
    try:
        # طلب درجة الحرارة من المستخدم
        temp = float(input("Enter the temperature to convert: "))
        # طلب الوحدة
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # التحقق من الوحدة وإجراء التحويل المناسب
        if unit == 'F':
            # تحويل من فهرنهايت إلى سيليزيوس
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        elif unit == 'C':
            # تحويل من سيليزيوس إلى فهرنهايت
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

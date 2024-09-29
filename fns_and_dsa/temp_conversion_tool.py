# تعريف المتغيرات العامة لعوامل التحويل
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32  # فرق التحويل للدرجات فهرنهايت

# دالة التحويل من فهرنهايت إلى مئوية
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# دالة التحويل من مئوية إلى فهرنهايت
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET
    return fahrenheit

# الدالة الرئيسية للتفاعل مع المستخدم
def main():
    try:
        # طلب درجة الحرارة من المستخدم
        temp = float(input("Enter the temperature to convert: "))

        # تحديد وحدة القياس (مئوية أو فهرنهايت)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # تحويل درجة الحرارة بناءً على الوحدة
        if unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")
        else:
            print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
    
    # التعامل مع الأخطاء في حالة إدخال درجة حرارة غير صحيحة
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

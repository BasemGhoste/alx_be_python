# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Perform safe division handling ZeroDivisionError and ValueError."""
    try:
        # محاولة تحويل المدخلات إلى أرقام عشرية
        num = float(numerator)
        denom = float(denominator)
        
        # محاولة إجراء القسمة
        result = num / denom
        return f"The result of the division is {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

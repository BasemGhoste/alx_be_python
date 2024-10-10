class BankAccount:
    def __init__(self, initial_balance=0):
        """تهيئة رصيد الحساب عند إنشاء الحساب. الرصيد الافتراضي هو 0"""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """إضافة المبلغ إلى الرصيد"""
        self.account_balance += amount

    def withdraw(self, amount):
        """خصم المبلغ إذا كان الرصيد كافياً. إرجاع True إذا تمت العملية، وإلا إرجاع False"""
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """عرض الرصيد الحالي بطريقة مفهومة"""
        print(f"Current Balance: ${self.account_balance:.2f}")


# دالة لعرض القائمة الرئيسية
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# الدالة الرئيسية
def main():
    # بدء قائمة التسوق فارغة
    shopping_list = []

    # حلقة تكرارية حتى يختار المستخدم الخروج
    while True:
        display_menu()  # عرض القائمة
        choice = input("Enter your choice: ").strip()  # الحصول على اختيار المستخدم

        if choice == '1':
            # طلب إضافة عنصر إلى القائمة
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)  # إضافة العنصر إلى القائمة
            print(f"'{item}' has been added to your shopping list.")

        elif choice == '2':
            # طلب إزالة عنصر من القائمة
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)  # إزالة العنصر من القائمة
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in your shopping list.")  # في حالة عدم العثور على العنصر

        elif choice == '3':
            # عرض قائمة التسوق
            if shopping_list:
                print("Your current shopping list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            # إنهاء البرنامج
            print("Goodbye!")
            break

        else:
            # التعامل مع المدخلات غير الصحيحة
            print("Invalid choice. Please try again.")

# التأكد من أن البرنامج يعمل كبرنامج رئيسي
if __name__ == "__main__":
    main()

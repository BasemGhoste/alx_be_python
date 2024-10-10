# main.py

from library_management import Book, Library

def main():
    # إعداد مكتبة صغيرة
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # القائمة الأولية للكتب المتاحة
    print("Available books after setup:")
    library.list_available_books()

    # محاكاة استئجار كتاب
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # محاكاة إعادة كتاب
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()

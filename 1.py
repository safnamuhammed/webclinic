def find_length():
    print("Length =", len(s))


def upper_case():
    print("Uppercase =", s.upper())


def lower_case():
    print("Lowercase =", s.lower())


def reverse_string():
    print("Reverse =", s[::-1])


def check_palindrome():
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")


def count_vowels():
    count = 0

    for char in s:
        if char in "aeiouAEIOU":
            count += 1

    print("Number of Vowels =", count)


def replace_string():
    old = input("Enter substring to replace: ")
    new = input("Enter new substring: ")

    print("New String =", s.replace(old, new))


def search_string():
    sub = input("Enter substring to search: ")

    if sub in s:
        print("Substring Found")
    else:
        print("Substring Not Found")


def count_character():
    char = input("Enter character: ")
    print("Occurrence =", s.count(char))


s = input("Enter a string: ")

while True:
    print("\n----- MENU -----")
    print("1. Find Length")
    print("2. Convert to Uppercase")
    print("3. Convert to Lowercase")
    print("4. Reverse String")
    print("5. Check Palindrome")
    print("6. Count Vowels")
    print("7. Replace Substring")
    print("8. Search Substring")
    print("9. Count Character Occurrence")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        find_length()

    elif choice == 2:
        upper_case()

    elif choice == 3:
        lower_case()

    elif choice == 4:
        reverse_string()

    elif choice == 5:
        check_palindrome()

    elif choice == 6:
        count_vowels()

    elif choice == 7:
        replace_string()

    elif choice == 8:
        search_string()

    elif choice == 9:
        count_character()

    elif choice == 10:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")

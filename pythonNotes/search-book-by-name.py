# 01.07.2022, @author...

# search book by name
book_lst = ["python", "java", "html", "css", "javaScript", "DBMS", "OS", "OOPS", "Networking"]


# [print(book) for book in book_lst]  # using list_comprehension

# iterating by for loop,
# for i in range(len(book_lst)):
#     print(book_lst[i])


def show_available_book():
    print("available books are: ")
    for book in book_lst:
        print(book, end=" ")


def search_book_by_name():
    book_name = input("Enter book name: ")

    for book in range(len(book_lst)):
        if book_name == book_lst[book]:
            print(f"{book_name} is available")
    else:
        print("sorry!!!, the book you have searched not available")
        show_available_book()


dict_book = {
    "101": "java",
    "102": "python",
    "103": "HTML",
    "104": "CSS",
    "105": "javaScript"
}


def show_dict_book():
    print("available books:")
    for book in dict_book:
        print(dict_book[book], end=" ")

    print("\nbook by book_id: ", dict_book.keys())


# show_available_book()
# search_book_by_name()
# show_dict_book()


# =============================================================================================================
def reverse_number():
    number = 123  # here we declare and initializing variable, 'number'
    num = number
    reverse = 0

    while number != 0:
        remainder = number % 10  # (1)123 % 10: 3, (2)12 % 10: 2, (3)1 % 10: 1,
        reverse = reverse * 10 + remainder  # (1)store * 10 + 3: 30, (2)store = 30, 30 * 10 + 2: 32, 32 * 10 + 1: 321
        number = number // 10  # (1)123 // 10: 12, (2), (3), other_languages: (/): division_operator,
        # but in python we use(//)

    print(f"reverse_number ({num}): ", reverse, end="")
    print()


# reverse_number()


# ===============================================================================================================


# ===============================================================================================================
# up to 8th, we have (1st term): 1,     (2nd term):     1, we get next term by adding previous two term, 1 + 1 = 2,
# and so on up to required term.

#  1,    1,    2,     3,    5,    8,   13,   21,     length: 8
# 1st   2nd   3rd    4th   5th   6th  7th   8th ,    terms

# logic: let a[1st_term] = 1,  b[2nd_term] = 1,  a + b,  we get new_term, c, and so on we proceed further

def fibonacci_series_up_to_nth_term():
    number = 0
    term_a = term_b = 1

    while number != 8:
        new_term = term_a + term_b
        term_a, term_b = term_b, new_term
        print(new_term, end=" ")

        number += 1


# fibonacci_series_up_to_nth_term()

# ===============================================================================================================
def armstrong_number():
    number = "153"
    add = 0

    for i in range(0, len(number)):
        add += int(number[i]) ** len(number)

        if add == int(number):
            print("number is armstrong_number")
            exit()

    return "number is not armstrong"


# a number which sum is,  power of each digit acc. to number_length, equals to that number
#  let 153, length is: 3, so power raise to each digit is: 3, so 1^3[3] + 5^3[125] + 3^3[27] = 153

# print(armstrong_number())


# =================================================================================================================

# palindrome number, tha number which is equals that number after reversing the number, i.e: 121 == 121(reverse)

def palindrome():
    data = "madam"

    if type(data) == int:
        data = str(data)

    if data == data[::-1]:
        print(f"{data}, {type(data)} is palindrome")
        exit()

    return f"{data}, [{type(data)}] is not palindrome"


print(palindrome())



def is_palindrome(input_list):
    list = input_list[::-1]
    if list == input_list:
        print("This List are  palindrome")
    else:
        print("This List are not palindrome")


def is_palindrome1(input_list):
    list = input_list
    list.reverse()
    if input_list == list:
        print("This List are  palindrome")
    else:
        print("This List are not palindrome")


List = [1, 2, 3, 2, 1]
is_palindrome(List)
is_palindrome1(List)

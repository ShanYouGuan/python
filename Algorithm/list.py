def is_palindrome(List):
    list = List[::-1]
    if list == List:
        print("This List are  palindrome")
    else:
        print("This List are not palindrome")
def is_palindrome1(List):
    list = List
    list.reverse()
    if List == list:
        print("This List are  palindrome")
    else:
        print("This List are not palindrome")
List = [1, 2, 3, 2, 1]       
is_palindrome(List)
is_palindrome1(List)
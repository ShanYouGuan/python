

def is_palindrome(input_list):
    list = input_list[::-1]
    if list == input_list:
        print("This List are  palindrome")
    else:
        print("This List are not palindrome")


def show_list(input_list):
    for i in range(0, len(input_list)):
        print(i)


def is_palindrome1(input_list):
    list = input_list
    list.reverse()
    if input_list == list:
        print("This List are  palindrome")
    else:
        print("This List are not palindrome")


def is_palindrome2(input_list):
    new_list = []
    for i in range(0, len(input_list)):
        new_list.append(input_list[len(input_list)-1-i])
    if new_list == input_list:
        print("This List are  palindrome")
    else:
        print("This List are not palindrome")


def return_list(List):
    return List


List = [1, 2, 3, 2, 1]
is_palindrome(List)
is_palindrome1(List)
is_palindrome2(List)
show_list(List)
return_list(List)
print('这是在my-work分支上做修改')
print('2020-11-13')

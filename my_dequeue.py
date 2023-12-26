from collections import deque


def is_palindrome(s):
    s = s.lower()
    char_deque = deque(s)
    result = True
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            result = False
            break
    if result:
        print(f'The string "{s}" is a palindrome.')
    else:
        print(f'The string "{s}" is not a palindrome.')


is_palindrome("test")
is_palindrome("dad")

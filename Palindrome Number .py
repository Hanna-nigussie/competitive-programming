def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

num = int(input())
print(isPalindrome(num))

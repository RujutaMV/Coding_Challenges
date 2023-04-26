def check_palindrome(s: str) -> bool:
    """
    Check if the given string is a palindrome
    Palindrome: original string and reverse is exactly identical
    eg: civic, radar, racecar
    :param s: str
    :return: bool
    """
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False


q10_output = check_palindrome("Was it a car or a cat I saw")
print(f'{q10_output=}')   # even if alphabets match, spaces do not match
q10_output = check_palindrome("Radar")
print(f'{q10_output=}')

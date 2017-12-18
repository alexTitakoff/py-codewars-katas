# https://www.codewars.com/kata/single-character-palindromes/train/python

# You will be given a string and you task is to check if
# it is possible to convert that string into a palindrome
# by removing a single character. If the string is already
# a palindrome, return "OK". If it is not, and we can convert
# it to a palindrome by removing one character, then return
# "remove one", otherwise return "not possible". The order of
# the characters should not be changed.


# я думал что просто убрать с конца или начала. А тут про то что любую букву можноли убрать чтобы было норм


# solve("abba") = "OK". -- This is a palindrome
# solve("abbaa") = "remove one". -- remove the 'a' at the extreme right.
# solve("abbaab") = "not possible".



def solve(s):
    if s == s[::-1]:
        print("OK")
        return "OK"

    i = 0
    for ch in s:
        new_s = s[:i] + s[i + 1:]
        if new_s == new_s[::-1]:
            print('remove one')
            return "remove one"
        i += 1

    print("not possible")
    return "not possible"


# solve("abba")
solve("hannah")




# Best pratices

# def solve(s):
#     isOK = lambda x: x == x[::-1]
#
#     return ("OK" if isOK(s)  else
#             "remove one" if any(isOK(s[:i] + s[i + 1:]) for i in range(len(s))) else
#             "not possible")

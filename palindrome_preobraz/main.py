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
    elif s[:-1] == s[:-1][::-1]:
        print('remove one')
        return 'remove one'
    elif s[1:] == s[1:][::-1]:
        print('remove one')
        return 'remove one'
    else:
        print('not possible')
        return 'not possible'


# solve("abba")
solve("madmam")
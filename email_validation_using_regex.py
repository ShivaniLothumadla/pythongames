"""
1.length should be atleast 8 chars
2.{.} should be in either in -3 or -4
3.only one @ symbol should present
4.first char should be an alpha bet
5. no space should be entertained
6. first char should be lowercase
7.all should be in lower case
6. {_,.,@} only allowed
"""
"""
regular expression have 3 main methods
1.match:
syntax:re.match(r'pattern', string, flags)
here flags is optional
match is used to search for the given pattern in beginning of the given string.
search is used to search for the given pattern in entire string but gives the first occurancce though we have multiple matches.
search is also having same syntax like match.
findall:
is used to search for the given pattern in entire string and gives all occurances of the pattern.
"""
import re
email = input('enter your mail: ')
email_validation = r'^[a-zA-Z]+[_.]?[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}$'
if re.search(email_validation, email):
    print('Right email')
else:
    print('wrong email')

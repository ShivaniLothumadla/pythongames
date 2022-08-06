"""
1.length should be atleast 8 chars
2.{.} should be in either in -3 or -4
3.only one @ symbol should present
4.first char should be an alpha bet
5. no space should be entertained
6. first char should be lowercase
7.all should be in lower case

6. {_,.,@} only allowed
7.
"""
email = input("Enter an email: ")
s = d = 0
if len(email) < 8:
    print(f'please enter atleast {8} characters, you have entered {len(email)} characters')
else:
    if email[0].isalpha():
        if (email[-3] == '.') ^ (email[-4] == '.'):
            if '@' in email and email.count('@') == 1:
                for i in email:
                    if i.isspace():
                        s = 1
                    elif i.isalpha():
                        continue
                    elif i == '.' or i == '@' or i == '_':
                        continue
                    elif i.isdigit():
                        continue
                    else:
                        d = 1
                if s == 1 or d == 1:
                    if s == 1:
                        print('spaces not allowed in email')
                    else:
                        print('only [_,@,.] are allowed, you have entered {i}')
                else:
                    print('The email you have entered is correct:)')
            else:
                print(f'@ symbol should be present 1 time in email')
        else:
            print('{.} should be present at 4th position or 3rd position from the last and it should not be present at both posotions.')
    else:
        print(f'first character should be an alphabet, you have entered a digit')

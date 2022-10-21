import re
s = input()
if re.fullmatch(r"^([a-z]{2}[0-9]{3}[a-z]{1})?$", s) or re.fullmatch(r"^([A-Z]{2}[0-9]{3}[A-Z]{1})?$", s):
    print('yes')
else:
    print('no')

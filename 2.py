s = input()
s = s.strip()
s = s[:1].upper() + s[1:].lower()
if s[-1:] == '!' or s[-1:] == '?':
    print(s[:-1] + '.')
elif s[-3:] == '...':
    print(s[:-2])
elif s.endswith('.') == True:
    print(s)
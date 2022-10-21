s1, s2 = input().split()
count = s1.count(s2)
s1 = s1.replace(s2, '', count - 1)
print(s1)
b = '<>\/?'
while 1:
    s = input()
    if s != '':
        if s[-3:] == 'txt' or s[-3:] == 'doc' or s[-4:] == 'docx' or s[-3:] == 'odt' or s[-3:] == 'rtf':

            for i in s:
                if i in b:
                    print('не может')
                    break
            else:
                print('может')
        else:
            print('не может')
    else:
        print('не может')

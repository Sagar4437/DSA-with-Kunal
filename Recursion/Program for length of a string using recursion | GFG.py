def strlen(str):
    if str == '':
        return 0
    else:
        return 1 + strlen(str[1:])

print(strlen('sagar')) 

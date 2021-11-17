def timeConversion(s):
    hour=int(s[0:2])
    is_pm=s[-2:]
    if is_pm=="PM":
        hour= hour if hour==12 else hour+12
        return "{0:02d}".format(hour)+s[2:-2]
    else:
        if hour==12:
            hour=0
        return "{0:02d}".format(hour)+s[2:-2]

s=input()
print(timeConversion(s))

def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup

dayfactor=0.01

while dayUP(dayfactor) < 37.2:
    dayfactor += 0.001

print("需要每天努力工作的程度是{:.3f}".format(dayfactor))

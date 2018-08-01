strawberries=input("how many strawberries they have?")

weekday=True
weekend=True

strday=str(strawberries > 39 and strawberries < 61)
strend=str(strawberries > 39)
if strawberries==(strday and weekday) or (strend and weekend):
    print('fun')
else:
    print('not fun')

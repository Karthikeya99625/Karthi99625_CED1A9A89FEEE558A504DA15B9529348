def isleapyear(year):
if (year % 4) == 0 and (year %100)!= 0 or (year % 400) == 0:
  return ture
else:
  return False
  year=(int(input()))
  if isleapyear (year):
    print ("{} is a leap year". format (year))
  else:
    print ("{} is not a leap year". formai(isleapyear))
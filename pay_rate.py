Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> hour = input("Enter total overtime hours. "); rate = input("Enter pay rate. "); print(str(hour) * str(rate) * 1.5)
Enter total overtime hours. 45
Enter pay rate. 10
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    hour = input("Enter total overtime hours. "); rate = input("Enter pay rate. "); print(str(hour) * str(rate) * 1.5)
TypeError: can't multiply sequence by non-int of type 'str'
>>> hour = input("Enter total overtime hours. "); rate = input("Enter pay rate. "); pay = int(hour) * int(rate) * 1.5
Enter total overtime hours. 45
Enter pay rate. 10
>>> print(str(pay))
675.0
>>> 

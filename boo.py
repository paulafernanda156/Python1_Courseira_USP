Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5 > 3
True
>>> 18 == 9 * 2
True
>>> 
>>> x = 12312
>>> x < 0
False
>>> 
>>> type(False)
<class 'bool'>
>>> type (x > 0)
<class 'bool'>
>>> x > 0 and x ** 2 > 100
True
>>> (x != 0) and (x ==0)
False
>>> True and (4 => 3)
SyntaxError: invalid syntax
>>> (-10 <x <0)
False
>>> (x>0) or (x <= 0)
True
>>>  x = 5
 
SyntaxError: unexpected indent
>>> x = 5
>>> y = 3
>>> x > y
True
>>> x = 5
>>> y = 3
>>> z = 7
>>> x > y and x < z
True
>>> idade=15
>>> idade = 15
>>> mairidade = 18
>>> pode_dirigir = idade >= maioridade
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    pode_dirigir = idade >= maioridade
NameError: name 'maioridade' is not defined
>>> maioridade = 18
>>> pode_dirigir = idade >= maioridade

>>> print (pode dirigir)
SyntaxError: invalid syntax
>>> 
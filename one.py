try:
  answer = input('Выбери действие: 1 - Перевести число из десятичной в двоичную систему\n')
except SyntaxError:
    print("Введите число!!!")
try:
  x = int(input("Введи число: "))
except:
    print("Введите число!!!")

y = 2
my_list = {}
q = 0
var = q

def func1():
  global x
  global q
  global var
  global my_list
  global y

  while int(x) > 0:
    z = int(x % y)
    x /= 2
    my_list[var] = z
    q += 1
    var = q

  reversed(my_list)
  print("".join(f'{v}' for v in my_list.values()))

if answer == str(1):
    func1()

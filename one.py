

y = 2
my_list = {}
q = 0
var = q
anim = "."

def func1():
  global q
  global var
  global my_list
  global y
  global anim

  try:
    x = int(input("Введи число: "))
  except:
    print("Введите число!!!")

  while int(x) > 0:
    z = int(x % y)
    x /= 2
    my_list[var] = z
    q += 1
    var = q
    print(anim)
    anim += "."

  print("Успешно выполнено!")

  reversed(my_list)
  print("".join(f'{v}' for v in my_list.values()))

  # Очистка
  y = 2
  my_list = {}
  q = 0
  var = q
  anim = "."

  mainfunc()

def mainfunc():
  try:
    answer = input('Выбери действие: 1 - Перевести число из десятичной в двоичную систему\n')
  except SyntaxError:
      print("Введите число!!!")
  if answer == str(1):
      func1()

mainfunc()
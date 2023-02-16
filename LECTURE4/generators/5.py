N = int(input())
class MyNumbers:
  def __iter__(self):
    self.a = N
    return self

  def __next__(self):
    if self.a >= 0:
      x = self.a
      self.a -= 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
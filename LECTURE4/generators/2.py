N = int(input())
class MyNumbers:
  def __iter__(self):
    self.a = 0
    return self

  def __next__(self):
    if self.a <= N:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    if(x % 2 == 0):
        if(x!=N and x!=N-1 ):
         print(x, end=', ')
        else:
         print(x)
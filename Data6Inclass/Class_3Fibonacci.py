# first second third
# -1      1       0
# 1       0       1
#. 0      1       1
# 1        1      2
#. ....

# every_element = sum of previous two elements
class Fibonacci:
  def __iter__(self):
    self.first = -1
    self.second = 1
    return self
  def __next__(self):
    self.third = self.first + self.second
    self.first = self.second
    self.second = self.third
    return self.third
    # -1 + 1 = 0
    # next-> +1 + 0

    
myseries = Fibonacci()
mynums = iter(myseries)
for i in range(10):
  print(next(mynums))

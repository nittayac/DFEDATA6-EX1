
class LinearSeries:
  def __iter__(self):
    self.num = 1 # starting point
    return self
  def __next__(self):
    self.num = self.num + 1 # how to calculate the next element
    return self.num


# or
#class LinearSeries:
#  def __iter__(self):
#    self.num = 0 # starting point
#    return self
#  def __next__(self):
#    self.num = self.num + 1 # how to calculate the next element
#    return self.num
# or
#class LinearSeries:
#  def __iter__(self):
#    self.num = 0 # starting point
#    return self
#  def __next__(self):
#    self.num = self.num + 1 # how to calculate the next element
#    return self.num
myseries = LinearSeries()
randompointer = iter(myseries)


# the starting point of series
next(randompointer)
next(randompointer)
next(randompointer)
myseries = LinearSeries()
randompointer = iter(myseries)


# the starting point of series
next(randompointer)
next(randompointer)
next(randompointer)


#or use for
for i in range(10):
  print(next(randompointer))

# Geographic point-> lati, long
# a,b -> remember 2 names; operate on 2 names
# CLASS 

# functional-> functions
# how to do things
# 1. Switch on the fan _ def fan_on():
# 2. change the speed def change_speed():
# 3. switch off the fan def fan_off():

# Objected oriented-> classes 
# IDENTIFY-> NOUN, VERBS
# CLASS FAN-> can perform 3 functions
# class Fan:
# def switch_on, change_speed, switch_off
# Fan f1; f1.on(). 
# OBJECTS

class Human:
  def speak(this):
    print('bye bye')
  def jump(this):
    return "i jumped. Bye bye."
  def eat(this, food):
    return food-1

#Human-> 1 nose
# 3 noses;
class Human:
  def __init__(self): # called automatically 
    self.noseCount = 1
    self.tailCount = 0
  def getLimbCount(self):
    print('Nose count = ' + str(self.noseCount))
    print('Tail count = ' + str(self.tailCount))


john = Human()
print(dir(john))
john.getLimbCount()

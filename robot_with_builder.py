from abc import ABC, abstractmethod  # For Builder classes

# Doesn't need an endless list of arguments when initialized
class Robot:
  # Uses a lot of flag logic here:  Is that necessary?
  # Does the use of this flag logic create other problems?
  def __init__(self):
    self.bipedal = False
    self.quadripedal = False
    self.wheeled = False
    self.flying = False
    self.traversal = []
    self.detection_systems = []

  # Huge decision statement: why is this not good?
  # Can we improve this?
  def __str__(self):
    string = ""
    if self.bipedal:
      string += "BIPEDAL "
    if self.quadripedal:
      string += "QUADRIPEDAL "
    if self.flying:
      string += "FLYING ROBOT "
    if self.wheeled:
      string += "ROBOT ON WHEELS\n"
    else:
      string += "ROBOT\n"

    if self.traversal:
      string += "Traversal modules installed:\n"

    for module in self.traversal:
      string += "- " + str(module) + "\n"

    if self.detection_systems:
      string += "Detection systems installed:\n"

    for system in self.detection_systems:
      string += "- " + str(system) + "\n"

    return string

#---------------------------------------------------------------------------

# Concrete classes for componenets
# In a real application, there would be an endless list of these, each one
#   composing additional subcomponents
class BipedalLegs:
  def __str__(self):
    return "two legs"

class QuadripedalLegs:
  def __str__(self):
    return "four legs"

class Arms:
  def __str__(self):
    return "two arms"

class Wings:
  def __str__(self):
    return "wings"

class Blades:
  def __str__(self):
    return "blades"

class FourWheels:
  def __str__(self):
    return "four wheels"

class TwoWheels:
  def __str__(self):
    return "two wheels"

class CameraDetectionSystem:
  def __str__(self):
    return "cameras"

class InfraredDetectionSystem:
  def __str__(self):
    return "infrared"

#----------------------------------------------------------------------------
# Note that this code was place at the top of this program for visibility
#from abc import ABC, abstractmethod

# The abstract superclass for all the builders
# We're using inheritence, but it's shallow
class RobotBuilder(ABC):
    
  @abstractmethod
  def reset(self):
    pass

  @abstractmethod
  def build_traversal(self):
    pass

  @abstractmethod
  def build_detection_system(self):
    pass

    
# Concrete Builder class:  there would be MANY of these
class AndroidBuilder(RobotBuilder):
  def __init__(self):
    self.product = Robot()

  def reset(self):
    self.product = Robot()

  # All of the concrete builders have this in common
  # Should it be elevated to the superclass?  
  def get_product(self):
    return self.product

  def build_traversal(self):
    self.product.bipedal = True
    self.product.traversal.append(BipedalLegs())
    self.product.traversal.append(Arms())

  def build_detection_system(self):
    self.product.detection_systems.append(CameraDetectionSystem())

# Concrete Builder class:  there would be many of these
class AutonomousCarBuilder(RobotBuilder):
  def __init__(self):
    self.product = Robot()

  def reset(self):
    self.product = Robot()

  # All of the concrete builders have this in common
  # Should it be elevated to the superclass?  
  def get_product(self):
    return self.product

  def build_traversal(self):
    self.product.wheeled = True
    self.product.traversal.append(FourWheels())

  def build_detection_system(self):
    self.product.detection_systems.append(InfraredDetectionSystem())

#-------------------------------------------------------------------------
#'''
# Remove # in line above to comment out this section when using Director

# Using the builders to create different robots
builder = AndroidBuilder()
builder.build_traversal()
builder.build_detection_system()
print(builder.get_product())

builder = AutonomousCarBuilder()
builder.build_traversal()
builder.build_detection_system()
print(builder.get_product())

#-------------------------------------------------------
#  Keep line below whether testing builders or director
'''
#-------------------------------------------------------

# Diretor manages all of the Builders
# Do we need separate make methods?
class Director:
    def make_android(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

    def make_autonomous_car(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

director = Director()

builder = AndroidBuilder()
print(director.make_android(builder))

builder = AutonomousCarBuilder()
print(director.make_autonomous_car(builder))

# comment out line below when testing director
'''


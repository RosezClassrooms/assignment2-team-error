# In order to only give values for relevant attributes, you must
#   use some form of keyword argument initialization
# However, all of the attributes must be given default values
# Keep in mind that in a real application, these would be endless ...

# Is there any danger in having users decide which attributes to specify?
# What about organization and readability?  Should they all be in one place?
# Even if you didn't apply Builder, are there ways to improve this
#   keyword implementation?
class Robot:
  def __init__(self, bipedal = None, quadripedal = None, wheeled = None,
             flying = None, traversal = [], detection_systems = []):
    self.bipedal = bipedal
    self.quadripedal = quadripedal
    self.wheeled = wheeled
    self.flying = flying
    self.traversal = traversal
    self.detection_systems = detection_systems

  # This is still awful!  What should we do about it??
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

# Concrete component classes
# If they are defined at this level, they would multiply like rabbits in a
#   real system, and would have an endless list of subcomponents also
# Are there better ways to manage all these components?
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


# Constructing robots by providing only relevant attributes
# Note that when providing attributes via keyword, order doesn't matter!
# Is there a danger here??
biped = BipedalLegs()
android = Robot(detection_systems = [CameraDetectionSystem()],
                bipedal = biped, traversal = [biped, Arms()] )
print(android)

wheels = FourWheels()
auto_auto = Robot(detection_systems = [InfraredDetectionSystem()],
                  wheeled = wheels, traversal = [wheels])
print(auto_auto)

flyer = Wings()
flying_monkey_robot = Robot(
  detection_systems = [CameraDetectionSystem(), InfraredDetectionSystem()],
  flying = flyer, traversal = [flyer, Arms()])
print(flying_monkey_robot)

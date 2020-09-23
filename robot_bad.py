# Motivation for Builder
# If this were a real application it would probably have to deal with an 
#   endless list of attributes to configure
# Note:  this code is not meant to be run!

class Robot:
  def __init__(self, left_leg, right_leg, left_arm, right_arm,
               left_wing, right_wing, tail, blades, cameras,
               infrared_module #, ...
               ):
    self.left_leg = left_leg
    if left_leg == None:
        bipedal = False
    self.right_leg = right_leg
    self.left_arm = left_arm
    self.right_arm = right_arm
    # ...


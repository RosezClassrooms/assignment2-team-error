from abc import ABC, abstractmethod  # For Builder classes
from enum import Enum

RobotTraversal = Enum('RobotTraversal', 'bipedal quadripedal wheeled flying')
RobotTraversalSystem = Enum('RobotTraversalSystem', 'bipedal_legs quadripedal_legs wings blades two_wheels four_wheels arms')
RobotDetectionSystem = Enum('RobotDetectionSystem', 'camera_detection_system infrared_detection_system')
# Doesn't need an endless list of arguments when initialized
class Robot:
    # Uses a lot of flag logic here:  Is that necessary?
    # Does the use of this flag logic create other problems?

    def __init__(self):
        self.traversal = None
        self.traversal_systems = []
        self.detection_systems = []

    def __str__(self):
        
        string = "Robot is " + str(self.traversal.name) + "\n"  

        if self.traversal_systems:
          string += "Traversal modules installed:\n"
        i = 0
        for module in self.traversal_systems:
            if(type(module) == list):
              string += "- " + str(module.name[i]) + "\n"
              i += 1
            else:
              string += "- " + str(module.name) + "\n"
        i = 0          
        if self.detection_systems:
          string += "Detection systems installed:\n"

        for system in self.detection_systems:
            if(type(system) == list):
              string += "- " + str(system[i].name) + "\n"
              i += 1
            else:
              string += "- " + str(system.name) + "\n"

        return string


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
        traversal_items = (RobotTraversalSystem.bipedal_legs, RobotTraversalSystem.arms)
        self.product.traversal_systems.append(RobotTraversalSystem.bipedal_legs)
        self.product.traversal_systems.append(RobotTraversalSystem.arms)
        self.product.traversal = RobotTraversal.bipedal


    def build_detection_system(self):
        self.product.detection_systems.append(RobotDetectionSystem.camera_detection_system)



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
        self.product.traversal_systems.append(RobotTraversalSystem.four_wheels)
        self.product.traversal = RobotTraversal.wheeled

    def build_detection_system(self):

        self.product.detection_systems.append(RobotDetectionSystem.infrared_detection_system)



# Diretor manages all of the Builders
# Created one make_robot method for all builders since the builder type i different
class Director:
    def make_robot(self,builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()


director = Director()

builder = AndroidBuilder()
print(director.make_robot(builder))

builder = AutonomousCarBuilder()
print(director.make_robot(builder))

# comment out line below when testing director

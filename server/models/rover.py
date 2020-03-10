import re

class Rover:
    x = 0
    y = 0
    d = ''

def verify_input(Input):
    Map = re.findall("(\d+\s+\d+)\n",Input)
    Start = re.findall("(\d+\s+\d+\s+[NSEW])\W+[LRM]+", Input)
    Instructions = re.findall("\d+\s+\d+\s+[NSEW]\W+([LRM]+)", Input)

    if len(Map) == 1:
        pass
    else:
        return 0

    if len(Start) > 0:
        pass
    else:
        return 0

    if len(Instructions) > 0:
        pass
    else:
        return 0

    return 1



class DeployRovers:
    rovers = []

    def __init__(self, Input):
        self.map = re.findall("(\d+\s+\d+)\n",Input)
        self.start = re.findall("(\d+\s+\d+\s+[NSEW])\W+[LRM]+", Input)
        self.instructions = re.findall("\d+\s+\d+\s+[NSEW]\W+([LRM]+)", Input)

    def roam(self):
        while len(self.start)>0:
            rover = Rover()
            start = self.start.pop(0).split(' ')
            rover.x = int(start[0])
            rover.y = int(start[1])
            rover.d = start[2]
            instructions = self.instructions.pop(0)
            for instruction in instructions:
                if instruction == 'L':
                    self._turn_left(rover)
                elif instruction == 'R':
                    self._turn_right(rover)
                elif instruction == 'M':
                    self._waddle_on(rover)
            self.rovers.append(rover)

    def _turn_left(self, rover):
        if rover.d == 'N':
            rover.d = 'W'
        elif rover.d == 'S':
            rover.d = 'E'
        elif rover.d == 'E':
            rover.d = 'N'
        elif rover.d == 'W':
            rover.d = 'S'

    def _turn_right(self, rover):
        if rover.d == 'N':
            rover.d = 'E'
        elif rover.d == 'S':
            rover.d = 'W'
        elif rover.d == 'E':
            rover.d = 'S'
        elif rover.d == 'W':
            rover.d = 'N'

    def _waddle_on(self, rover):
        if rover.d == 'N':
            rover.y = rover.y + 1
        elif rover.d == 'S':
            rover.y = rover.y - 1
        elif rover.d == 'E':
            rover.x = rover.x + 1
        elif rover.d == 'W':
            rover.x = rover.x - 1

def stringify_rovers(rovers):
    rover_list = []
    while (len(rovers) > 0):
        rover = rovers.pop(0)
        rover_list.append(f'{rover.x} {rover.y} {rover.d}')
    return rover_list

def run_rover_mission(Input):
    deployed_rovers = DeployRovers(Input)
    deployed_rovers.roam()
    return stringify_rovers(deployed_rovers.rovers)

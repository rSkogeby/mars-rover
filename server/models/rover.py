import re

class DeployRovers:

    def __init__(self, Input):
        self.map = re.findall("(\d+\s+\d+)\s+\W",Input)
        self.start = re.findall("(\d+\s+\d+\s+[NSEW])\W+[LRM]+", Input)
        self.instructions = re.findall("\d+\s+\d+\s+[NSEW]\W+([LRM]+)", Input)

def main(Input):
    deployed_rovers = DeployRovers(Input)

import unittest
from models.rover import DeployRovers, Rover

class TestRover(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rover = Rover()
        self.deploy_rover = DeployRovers('')

    def test_left_turn(self):
        self.rover.d = 'N'
        self.deploy_rover._turn_left(self.rover)
        self.assertEqual(self.rover.d, 'W')
        self.deploy_rover._turn_left(self.rover)
        self.assertEqual(self.rover.d, 'S')
        self.deploy_rover._turn_left(self.rover)
        self.assertEqual(self.rover.d, 'E')
        self.deploy_rover._turn_left(self.rover)
        self.assertEqual(self.rover.d, 'N')

    def test_right_turn(self):
        self.rover.d = 'N'
        self.deploy_rover._turn_right(self.rover)
        self.assertEqual(self.rover.d, 'E')
        self.deploy_rover._turn_right(self.rover)
        self.assertEqual(self.rover.d, 'S')
        self.deploy_rover._turn_right(self.rover)
        self.assertEqual(self.rover.d, 'W')
        self.deploy_rover._turn_right(self.rover)
        self.assertEqual(self.rover.d, 'N')

    def test_waddle_on(self):
        self.rover.d = 'N'
        self.deploy_rover._waddle_on(self.rover)
        self.assertEqual(self.rover.d, 'N')
        self.assertEqual(self.rover.y, 1)
        self.assertEqual(self.rover.x, 0)
        self.deploy_rover._waddle_on(self.rover)
        self.assertEqual(self.rover.d, 'N')
        self.assertEqual(self.rover.y, 2)
        self.assertEqual(self.rover.x, 0)
        self.deploy_rover._waddle_on(self.rover)
        self.assertEqual(self.rover.d, 'N')
        self.assertEqual(self.rover.y, 3)
        self.assertEqual(self.rover.x, 0)
        self.rover.d = 'E'
        self.deploy_rover._waddle_on(self.rover)
        self.assertEqual(self.rover.d, 'E')
        self.assertEqual(self.rover.y, 3)
        self.assertEqual(self.rover.x, 1)




if __name__ == "__main__":
    unittest.main()

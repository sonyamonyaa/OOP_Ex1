import unittest
from Elevator import Elevator


class ElevatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.el1 = Elevator(1, 1, 1, 1, 1)

    def test_speed(self):
        self.assertEqual(self.el1.speed, 1)
        # test default
        el0 = Elevator()
        self.assertEqual(el0.speed, 0)

    def test_time(self):
        # travel time to src and then to dest
        self.assertEqual(self.el1.time(2, 5), 7)
        # travel time to dest, already at src
        self.assertEqual(self.el1.time(0, 2), 5)
        # time to open/close
        self.assertEqual(self.el1.time(0, 0), 2)


if __name__ == '__main__':
    unittest.main()

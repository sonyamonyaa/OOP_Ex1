import unittest
import Call


class MyTestCase(unittest.TestCase):
    def test_call_init(self):
        c = Call.Call(1, 2)
        self.assertEqual(c.src, 1)
        self.assertEqual(c.dest, 2)

    def test_call_legit(self):
        low = 0
        top = 2
        c1 = Call.Call(1, 2)
        self.assertTrue(c1.is_legit(low, top))
        c2 = Call.Call(-1, 2)
        self.assertFalse(c2.is_legit(low, top))
        c2 = Call.Call(1, -2)
        self.assertFalse(c2.is_legit(low, top))


if __name__ == '__main__':
    unittest.main()

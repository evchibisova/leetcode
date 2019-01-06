import unittest
from task959 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertIsNone(self.s.regionsBySlashes([]))

    def test_wrong_symbols_in_grid(self):
        with self.assertRaises(ValueError, msg="Your grid contents unacceptable symbols"):
            self.s.regionsBySlashes(["q"])
            self.s.regionsBySlashes(["123"])

    def test_not_equal_sides(self):
        with self.assertRaises(ValueError, msg="Your grid has not equal sides"):
            self.s.regionsBySlashes("    ")

    def test_not_intersect_and_not_connect_borders_lines(self):
        self.assertEqual(0, self.s.regionsBySlashes(["\\ /",
                                                     "   ",
                                                     "/ \\"]))
        self.assertEqual(0, self.s.regionsBySlashes(["   ",
                                                     " / ",
                                                     "   "]))
        self.assertEqual(0, self.s.regionsBySlashes(["   ",
                                                     "/ /",
                                                     "   "]))

    def test_intersect_but_not_connect_borders_lines(self):
        self.assertEqual(0, self.s.regionsBySlashes(["    ",
                                                     " \\/ ",
                                                     " /\\ ",
                                                     "    "]))
        self.assertEqual(0, self.s.regionsBySlashes(["    ",
                                                     " /\\ ",
                                                     "    ",
                                                     "    "]))

    def test_not_intersect_but_connect_borders_lines(self):
        self.assertEqual(3, self.s.regionsBySlashes([" / ",
                                                     "/ /",
                                                     " / "]))
        self.assertEqual(3, self.s.regionsBySlashes(["/  ",
                                                     "   ",
                                                     "\\  "]))

    def test_intersect_and_connect_borders_lines(self):
        self.assertEqual(4, self.s.regionsBySlashes(["\\/",
                                                     "/\\"]))
        self.assertEqual(3, self.s.regionsBySlashes(["\\ ",
                                                     "/\\"]))
        self.assertEqual(2, self.s.regionsBySlashes(["\\/",
                                                     "  "]))

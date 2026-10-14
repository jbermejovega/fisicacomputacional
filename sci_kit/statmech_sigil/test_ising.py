import unittest
from ising import run, energy

class IsingTests(unittest.TestCase):
    def test_replay(self):
        self.assertEqual(run(4, 0.3, 10, 7), run(4, 0.3, 10, 7))
    def test_aligned_energy(self):
        self.assertEqual(energy([[1]*4 for _ in range(4)]), -32)
    def test_magnetization(self):
        self.assertLessEqual(abs(run(4, 0.5, 10, 1)["result"]["magnetization"]), 1)

if __name__ == "__main__":
    unittest.main()

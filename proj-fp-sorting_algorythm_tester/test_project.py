import unittest
import project
import inspect

class TestSum_project(unittest.TestCase):

    # Pretend to be a sorting module
    class algo(list):
        def sort(lst): lst.sort()

    def test_sorting_run(self):
        lst = [3, 5, 7, 2, 4, 6, 2, 3]
        x = lst.copy()
        x.sort() 
        y = project.sorting(lst.copy(), self.algo).run().list
        self.assertEqual(x, y)

    def test_algorythm_modules(self):

        # Test modules have sort function
        algos = project.algorythm_modules(project.IMPORTABLE)
        for algo in algos:
            self.assertTrue(hasattr(algo, 'sort') and inspect.isfunction(algo.sort))

        # Test all
        algos2 = project.algorythm_modules(['all'])
        self.assertEqual(algos, algos2)

        # Test not found
        self.assertRaises(SystemExit, project.algorythm_modules, ['unnamed_test'])

    def test_starting_list(self):
        
        # Sorted 10
        sor = project.starting_list(0, 10)
        self.assertEqual(len(sor), 10)
        self.assertEqual(sor, list(range(1, 11)))

        # Reversed 10
        rev = project.starting_list(1, 10)
        self.assertEqual(len(rev), 10)
        self.assertEqual(rev, list(range(10, 0, -1)))

        # Random 10
        ran = project.starting_list(2, 10)
        self.assertEqual(len(ran), 10)

        # Test 1000 times, because of randomness
        for _ in range(1000):
            self.assertLessEqual(max(ran), 10)
            self.assertGreaterEqual(min(ran), 1)


if __name__ == "__main__":
    unittest.main()
import test_debugger

from debugger import sort_list

class TestSortList(unittest.TestCase):

    def test_sort_list(self):
        x = [0,1,2,3,4,5,6,7,8]
        random.shuffle(x)
        self.assertEqual([0,1,2,3,4,5,6,7,8], sort_list(x))

        if __name__ == __main__:
            unittest.main




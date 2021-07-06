#from roguelikedev2021/..main import testing_func
#from ..actions import MovementAction
import actions
import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "Testing"
        expected = "Testing"
        self.assertEqual(actions.MovementAction(testcase), expected)
    pass

unittest.main()
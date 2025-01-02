import time
from unittest import TestCase
from exercise import fast_function, slow_function

class Evaluate(TestCase):

    def test_fast_function_speed(self):
        start_time = time.time()
        fast_function()
        end_time = time.time()
        speed = end_time - start_time
        self.assertAlmostEqual(speed, 0.1, delta=0.1, msg="fast_function must run in around 0.3s")

    def test_slow_function_speed(self):
        start_time = time.time()
        slow_function()
        end_time = time.time()
        speed = end_time - start_time
        self.assertAlmostEqual(speed, 1, delta=1, msg="slow_function must run in around 3s")
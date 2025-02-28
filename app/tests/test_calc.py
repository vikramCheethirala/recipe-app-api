from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    def test_add(self):
        res = calc.add(1,2)
        self.assertEquals(res,3)

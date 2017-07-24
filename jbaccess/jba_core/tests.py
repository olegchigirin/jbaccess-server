import datetime
from jba_core import pattern_evaluator
from django.test import TestCase


class PatternEvaluatorTest(TestCase):
    def setUp(self):
        pass

    def test_everyday_evaluation_inside_time_occurs_pattern(self):
        self.assertTrue(
            pattern_evaluator.pattern_eval_date(datetime.datetime(2017, 7, 5, 12, 0, 0), datetime.timedelta(hours=2),
                                                datetime.timedelta(hours=22), list(), list(), list()))

    def test_everyday_evaluation_outside_time_not_occurs_pattern(self):
        self.assertFalse(
            pattern_evaluator.pattern_eval_date(datetime.datetime(2017, 7, 5, 23, 0, 0), datetime.timedelta(hours=2),
                                                datetime.timedelta(hours=22), list(), list(), list()))

    def test_everywednesday_occurs_pattern(self):
        self.assertTrue(
            pattern_evaluator.pattern_eval_date(datetime.datetime(2017, 7, 5, 12, 0, 0), datetime.timedelta(hours=2),
                                                datetime.timedelta(hours=22), list([3]), list(), list()))

    def test_everywednesday_not_occurs_pattern(self):
        self.assertFalse(
            pattern_evaluator.pattern_eval_date(datetime.datetime(2017, 7, 6, 12, 0, 0), datetime.timedelta(hours=2),
                                                datetime.timedelta(hours=22), list([3]), list(), list()))

    def test_every5thday_occurs_pattern(self):
        self.assertTrue(
            pattern_evaluator.pattern_eval_date(datetime.datetime(2017, 7, 5, 12, 0, 0), datetime.timedelta(hours=2),
                                                datetime.timedelta(hours=22), list(), list([5]), list()))

    def test_every5thday_not_occurs_pattern(self):
        self.assertFalse(
            pattern_evaluator.pattern_eval_date(datetime.datetime(2017, 7, 6, 12, 0, 0), datetime.timedelta(hours=2),
                                                datetime.timedelta(hours=22), list(), list([5]), list()))

    def test_everyday_on_july_occurs_pattern(self):
        self.assertTrue(
            pattern_evaluator.pattern_eval_date(datetime.datetime(2017, 7, 5, 12, 0, 0), datetime.timedelta(hours=2),
                                                datetime.timedelta(hours=22), list(), list(), list([7])))

    def test_everyday_on_july_not_occurs_pattern(self):
        self.assertFalse(
            pattern_evaluator.pattern_eval_date(datetime.datetime(2017, 8, 5, 12, 0, 0), datetime.timedelta(hours=2),
                                                datetime.timedelta(hours=22), list(), list(), list([7])))

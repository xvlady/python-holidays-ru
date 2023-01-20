import unittest
from datetime import date

from holidays_ru import check_holiday, is_holiday


class TestBasics(unittest.TestCase):
    def test_deys(self):
        self.assertTrue(check_holiday(date(2023, 1, 1)))
        self.assertFalse(check_holiday(date(2023, 1, 12)))  # False
        self.assertTrue(check_holiday(date(2022, 1, 31)))
        self.assertFalse(
            check_holiday(date(2022, 1, 31), with_weekends=False)
        )  # False, it's Sunday
        self.assertEqual(is_holiday(date(2023, 1, 1)), "")  # "New Year's Day"
        self.assertEqual(is_holiday(date(2023, 1, 12)), "")  # ""
        self.assertEqual(is_holiday(date(2023, 1, 15)), "")  # "Weekend"
        self.assertEqual(is_holiday(date(2023, 1, 15)), "")  # "Moved weekend"
        self.assertEqual(
            is_holiday(date(2023, 1, 12)), ""
        )  # "", it's work Sunday

from unittest import TestCase
from pagination import make_pagination_range


class PaginationTest(TestCase):
    # current page = 1 - Qty Page = 2 - Middle page = 2
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)
    # current page = 2 - Qty Page = 2 - Middle page = 2
    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self): # noqa E999
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)
    # current page = 3 - Qty Page = 2 - Middle page = 2
    # HERE RANGE SHOULD CHANGE
    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self): # noqa E999
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3,
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)
    # current page = 4 - Qty Page = 2 - Middle page = 2
    # HERE RANGE SHOULD CHANGE
    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self): # noqa E999
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=4,
        )['pagination']
        self.assertEqual([3, 4, 5, 6], pagination)

    # current page = 10 - Qty Page = 2 - Middle page = 2
    # HERE RANGE SHOULD CHANGE
    def test_make_sure_middle_ranges_are_correct(self): # noqa E999
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=10,
        )['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)
    # current page = 12 - Qty Page = 2 - Middle page = 2
    # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=12,
        )['pagination']
        self.assertEqual([11, 12, 13, 14], pagination)

    # current page = 18 - Qty Page = 2 - Middle page = 2
    # HERE RANGE SHOULD CHANGE
    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=18,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)
    # current page = 20 - Qty Page = 2 - Middle page = 2
    # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=20,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)
    # current page = 20 - Qty Page = 2 - Middle page = 2
    # HERE RANGE SHOULD CHANGE
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=21,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

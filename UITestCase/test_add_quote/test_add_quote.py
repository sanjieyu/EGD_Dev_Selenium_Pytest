# Author: Yi Sun(Tim) 2024-06-16

'''Test Add Quote - Pytest Version'''

import pytest
from UIModule.add_quote import Add_Quote
# from UIModule.base_test import BaseTest

class Test_Add_Quote():

    def test_add_quote_001(self, add_quote):
        assert "http://xxxx/Quote/Create" in add_quote.check_addquote_url

    def test_add_quote_002(self, add_quote):
        assert ('Proposal Details','Contact Details','Site Details','Doors') == add_quote.check_defaulsection

    def test_add_quote_003(self, add_quote):
        assert add_quote.check_savequote_btn

    def test_add_quote_004(self, add_quote):
        assert ('Proposal Number','Pricing Category','User','Account Type','Order Date',
                          'Quote Status','Account Customer','Supply Type') == add_quote.check_proposal_details
# Author:Yi Sun(Tim) 2024-01-19

'''Test the Dealer Portal Page'''

import pytest
from UIModule.dealer_portal import *

class Test_Dealer_Portal():

    def test_dealer_portal_ui_001(self,dealer_portal):
        assert "http://xxxx/Dealer" in dealer_portal.check_dealer_url

    def test_dealer_portal_ui_002(self,dealer_portal):
        assert ("Create Quote","Search Quotes","ACCOUNT") == dealer_portal.check_default_values

    def test_dealer_portal_ui_003(self,dealer_portal):
        assert dealer_portal.check_find_dealer_quote is True

    def test_dealer_portal_ui_004(self,dealer_portal):
        assert ("tim2@tim.com","Log off") == dealer_portal.check_account_menu


if __name__ == '__main__':
    unittest.main(verbosity=2)

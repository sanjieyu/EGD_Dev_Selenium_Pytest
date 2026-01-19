# Author:Yi Sun(Tim) 2024-5-05

'''Test Add a Quote with a Custom door function'''

import pytest
from UIModule.add_quote_with_custom_door import Add_Quote_With_CustomDoor

class Test_Add_Quote_With_Customdoor():

    def test_add_quote_with_customdoor_001(self,add_quote_with_customdoor):
        '''Verify  Add a Quote with a Custom door function'''
        expected = ('Door 1(A1)','Quote')
        actual = add_quote_with_customdoor.verify_new_quote
        assert expected == actual,f"Expected:{expected},but got: {actual}"

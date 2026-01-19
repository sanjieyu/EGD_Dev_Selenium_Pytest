# Author:Yi Sun(Tim) 2024-5-05

'''Test Add a Insulated Door Functian'''

import pytest
from UIModule.add_insulated_door import Add_Insulated_Door

class Test_Add_Insulated_Door():

    def test_add_insulated_door_001(self,add_insulated_door):
        '''Verify the add insulate door function'''
        expected = ('1   Insulated Sectional, Ribline, Woodgrain Texture, Monument (2010 x 2560)')
        actual = add_insulated_door.new_added_door
        assert expected == actual,f"Expected:{expected},but got: {actual}"

    def test_add_insulated_door_002(self,add_insulated_door):
        '''Verify the duplicate button for the new added insulate door'''
        assert add_insulated_door.duplicate_btn is True

    def test_add_insulated_door_003(self,add_insulated_door):
        '''Verify the delete button for the new added insulate door'''
        assert add_insulated_door.delete_btn is True
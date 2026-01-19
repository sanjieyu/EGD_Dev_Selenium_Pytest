# Author:Yi Sun(Tim) 2024-4-16

import pytest
from UIModule.add_custom_door import Add_Custom_Door

class Test_Add_Custom_Door():

    def test_add_custom_door_001(self,add_custom_door):
        '''Verify the input validation when add a new door'''
        assert ("Errors\nFor current Headroom height, pelmet is required\nPanels Wide should be selected\nIf SR (left) "
                "is less than 89mm, LH Jamb should be minimum 90mm.\nIf SR (right) is less than 89mm, RH Jamb should be "
                "minimum 90mm.\nMotors field is required") == add_custom_door.validation_input

    def test_add_custom_door_002(self, add_custom_door):
        '''Verify the add door function'''
        add_custom_door.add_custom_detail()
        assert "Custom Door, Residential, OilColour (10 x 60)" == add_custom_door.new_added_custom_door

    def test_add_custom_door_003(self, add_custom_door):
        '''Verify the duplicate button for the new added door'''
        assert add_custom_door.duplicate_btn is True

    def test_add_custom_door_004(self, add_custom_door):
        '''Verify the delete button for the new added door'''
        assert add_custom_door.delete_btn is True
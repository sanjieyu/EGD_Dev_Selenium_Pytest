# Author:Yi Sun(Tim) 2023-11-02

'''Test  Add Custom Door Page - Pytest Version'''

import pytest
from UIModule.custom_door import Custom_Door

class Test_Custom_Door():

    def test_custom_door_001(self,custom_door):
        '''Verify the main elements in the page, should including correct title, Add button and Close button '''
        assert "Custom Door Details" == custom_door.check_customdoor_page

    def test_custom_door_002(self,custom_door):
        '''Verify each element for install details'''
        expected = ('Install Type','Design','Colour Category','Door Colour','Frame Colour','Timber Profile',
                    'Insert Material','Insert Location','Insert Type','Insert Colour','Insert Other','Custom Colour')
        actual = custom_door.check_install_details
        assert expected == actual,f"Expected:{expected},but got: {actual}"

    def test_custom_door_003(self, custom_door):
        '''Verify the Install Type dropdown list'''
        assert ("Please Select\nCommercial Cat 1\nCommercial Cat 2\nCommercial STD\nFull Panel Replacement\nResidential"
                == custom_door.check_install_type)

    def test_custom_door_004(self, custom_door):
        '''Verify the Design dropdown list'''
        assert ("Ali Batten\nAli Louvre Panel\nAliwood\nAlumalite\nAlumicomp\nBar panel\nBarn Panel\nCarriage Panel\n"
                "Cedar Batten\nCedar Panel 135\nCedar Panel 86\nClassic Panel\nFrame Only STD\nFrame Only Welded\n"
                "Glasslite\nGrille Panel\nHerringbone Panel\nLouvre Panel\nPerfalite\nRaised Panel\nRecessed Panel\n"
                "Tranquilo Panel\nTwinlight\nVerti Panel") in custom_door.check_design

    def test_custom_door_005(self, custom_door):
        '''Verify the Colour Category dropdown list'''
        assert ("Please Select\nCustom\nOilColour\nPainted\nPowderCoatStandard\nPowderCoatUpgrade\nPrimed\nRaw\n"
                "SealedColour" ==custom_door.check_colour_category)


    def test_custom_door_006(self, custom_door):
        '''Verify the Door Colour dropdown list should be diabled if select "Custom" in Colour Category'''
        assert custom_door.check_door_colour_custom is False

    def test_custom_door_007(self, custom_door):
        '''Verify the Door Colour dropdown if select "OliColour" in Colour Category '''
        assert "Please Select\nBlack Ash\nClear\nCustom\nSela Brown\nTBA" == custom_door.check_door_colour_oilcolour

    def test_custom_door_008(self, custom_door):
        '''Verify the Door Colour dropdown if select "Painted" in Colour Category '''
        assert "Please Select\nCustom Colour" == custom_door.check_door_colour_painted


    def test_custom_door_009(self, custom_door):
        '''Verify the Door Colour dropdown if select "Raw" in Colour Category '''
        assert "Please Select\nTBA" == custom_door.check_door_colour_raw


    def test_custom_door_010(self, custom_door):
        '''Verify the Door Colour dropdown if select "SealedColour" in Colour Category '''
        assert ("Please Select\nClear\nCustom\nDark oak\nEbony\nHemlock\nLight oak\nRosewood\nTBA\nWalnut" ==
                custom_door.check_door_colour_sealedcolour)

    def test_custom_door_011(self, custom_door):
        '''Verify the Frame Colour dropdown list '''
        assert ("Please Select\nClear\nCustom\nDark oak\nEbony\nHemlock\nLight oak\nRosewood\nTBA\nWalnut\nMill Finish"
                == custom_door.check_frame_colour)

    def test_custom_door_012(self, custom_door):
        '''Verify the Timber Profile dropdown list'''
        assert "Please Select\n135mm Shiplap\n135mm V-Join\n86mm Shiplap\n86mm V-Join" == custom_door.check_timber_profile

    def test_custom_door_013(self, custom_door):
        '''Verify the Insert Material dropdown list'''
        assert ("Please Select\nACPS Upgrade - Cat 1\nACPS Upgrade - Cat 2\nAcrylic\nAluminium\nExterier Ply\nGlass\n"
                "Other\nPolycarbonate\nStandard ACPS\nSupplied By Client\nTBA") == custom_door.check_insert_material

    def test_custom_door_014(self, custom_door):
        '''Verify the Insert Location dropdown list'''
        assert "Please Select\nFace Fixed\nInserted into Frame\nTBA" == custom_door.check_insert_location

    def test_custom_door_015(self, custom_door):
        '''Verify Insert Type dropdown list, the default value should be empty '''
        assert "Please Select" == custom_door.check_insert_type_default

    def test_custom_door_016(self, custom_door):
        '''Verify the Insert Type dropdown if select "ACPS Cat1" in Insert Material category'''
        assert "Please Select\nAlutile\nOther\nUltrabond\nVitrabond" == custom_door.check_insert_type_cat1

    def test_custom_door_017(self, custom_door):
        '''Verify the Insert Type dropdown if select "ACPS Cat2" in Insert Material category'''
        assert "Please Select\nAlpolic\nAlucabond\nOther\nSymonite" == custom_door.check_insert_type_cat2

    def test_custom_door_018(self, custom_door):
        '''Verify the Insert Type dropdown if select "Acrylic" in Insert Material category'''
        assert "Please Select\n3mm Acrylic\n4.5mm Acrylic\n6mm Acrylic" == custom_door.check_insert_type_acrylic

    def test_custom_door_019(self, custom_door):
        '''Verify the Insert Type dropdown if select "Aluminium" in Insert Material category'''
        assert (("Please Select\nCLOVERLEAF - 36%\nOther\nP1012SQ - 10mm Square-70%\nP1925 - 19mm Round-51%\n"
                 "P1931SR - 19x3mm slots-41%\nP2031 - 2MM Round-41%\nP2332HEX - 23mm Hexagon-44%\n"
                 "P2563SR - 25x6.3mm slots-43%\nP3247 - 3.2mm Round-41%\nP4763 - 4.7mm Round-51%\n"
                 "P4769 - 4.7mm Square-47%\nP5512SD - 5.5mm Square-19%\nP7995 - 7.9mm Round-62%\n"
                 "P9511HEX - 11.9mm Hexagon-64%")== custom_door.check_insert_type_aluminium)





# Author:Yi Sun(Tim) 2024-08-12

import pytest
from UIModule.standard_door import Standard_Door

class Test_Standard_Door():

    def test_standard_door_001(self,standard_door):
        '''Verify the main elements in the page, should including correct title, Add button and Close button '''
        expected = ('Standard Door Details', 'Add')
        actual  = standard_door.check_door_page
        assert expected == actual,f"Expected:{expected},but got: {actual}"

    def test_standard_door_002(self, standard_door):
        '''Verify each element for install details'''
        expected = ('Install Type', 'Door Type', 'Design', 'Colour Category', 'Door Colour', 'Door Finish',
                    'Custom Colour', 'Technician Measure', 'Measure Required')
        actual = standard_door.check_install_details
        assert expected == actual,f"Expected:{expected},but got: {actual}"

    def test_standard_door_003(self, standard_door):
        '''Verify the Install Type dropdown list'''
        assert ("Commercial Cat 1\nCommercial Cat 2\nCommercial STD\nFull Panel Replacement\nPanel Replacement\n"
                "Residential") in standard_door.check_install_type


    def test_standard_door_004(self, standard_door):
        '''Verify the Door Type dropdown list'''
        assert "Please Select\nExoRoll\nInsulated Sectional\nOptiLift\nOptiRoll\nPanel Lift-Safe" == standard_door.check_door_type


    def test_standard_door_005(self, standard_door):
        '''Verify the Colour Category dropdown list'''
        assert (("ColorBond\nColourbond Non Std\nCustom\nFlexigraphic\nFlexographic\nMetalFx\nOilColor\nPainted Finish\n"
                "Portabella\nPowderCoatStandard\nPowderCoatUpgrade\nSealedColor\nTimber Essence\nTimberFX") in
                standard_door.check_colour_category)

    def test_standard_door_006(self, standard_door):
        '''Verify the Design dropdown for Panel Lift-Safe Door'''
        assert "Slimline\nClassic panel\nLincoln panel\nUltraline\nWideline" in standard_door.check_design_panel


    def test_standard_door_007(self, standard_door):
        '''Verify the Design dropdown for Insulated Sectional Door'''
        assert "Ribline\nFineline\nFlatline\nStanford" in standard_door.check_design_insulated

    def test_standard_door_008(self, standard_door):
        '''Verify the Design dropdown for Roller Door'''
        assert "ExoRoll eS\nExoRoll eD\nExoRoll eC" in standard_door.check_design_roller


    def test_standard_door_009(self, standard_door):
        '''Verify the Door Colour dropdown for ColorBond Category'''
        assert ("Basalt\nBlue Gum\nClassic Cream\nCove\nDover White\nDune\nEvening Haze\nGully\nIronstone\nJasper\n"
                "Manor Red\nMonument\nNight Sky\nPaperbark\nShale Grey\nSoutherly\nSurfmist\nTBA\nWallaby\nWindspray\n"
                "Woodland Grey") in standard_door.check_colour_colorbond

    def test_standard_door_010(self, standard_door):
        '''Verify the Door Colour dropdown for Custom Category, should be disabled'''
        assert standard_door.check_colour_custom is True


    def test_standard_door_011(self, standard_door):
        '''Verify the Door Colour dropdown for Flexigraphic Category'''
        assert "Caoba Dawn\nClassic Cedar\nTBA" in standard_door.check_colour_flexigraphic


    def test_standard_door_012(self, standard_door):
        '''Verify the Door Colour dropdown for Flexographic Category'''
        assert "Caoba Dawn\nClassic Cedar\nTBA" in standard_door.check_colour_flexographic

    def test_standard_door_013(self, standard_door):
        '''Verify the Door Colour dropdown for MetalFx Category'''
        assert "Deep Bronze\nNew Copper\nPrecious Silver Pearl\nTBA" in standard_door.check_colour_metalfx


    def test_standard_door_014(self, standard_door):
        '''Verify the Door Colour dropdown for PaintedFinish Category'''
        assert ("Cottage Green\nCove\nDeep Ocean\nGully\nMangrove\nManor Red\nMonument Matt\nPale Eucalypt\nTerrain"
                in standard_door.check_colour_paintedfinish)


    def test_standard_door_015(self, standard_door):
        '''Verify the Door Colour dropdown for Portabella Category'''
        assert ("African Ebony\nEuropean Oak\nGolden Oak\nGrey Ironbark\nKnotted Walnut\nRed Gum\nTBA"
                in standard_door.check_colour_portabella)

    def test_standard_door_016(self, standard_door):
        '''Verify the Door Colour dropdown for TimberFX Category'''
        assert "Cedar\nJarrah\nTBA\nWalnut" in standard_door.check_colour_timberfx

    def test_standard_door_017(self, standard_door):
        '''Verify the Custom Colour input box'''
        assert standard_door.check_customcolour_box is True

    def test_standard_door_018(self, standard_door):
        '''Verify the Custom Colour input box'''
        assert standard_door.check_customcolourbox_custom is True

    def test_standard_door_019(self, standard_door):
        '''Verify each element for size details,'''
        expected = ('Opening Size LH', 'Opening Size RH', 'Opening Size Width', 'SR Left', 'HR', 'SR Right',
                    'LHRK (Required if HR is 200-269mm)')
        actual = standard_door.check_size_details
        assert expected == actual,f"Expected:{expected},but got: {actual}"

    def test_standard_door_020(self, standard_door):
        '''Verify the default value for Opening Size LH, should be "0" '''
        assert "0" == standard_door.check_openinglh_default

    def test_standard_door_021(self, standard_door):
        '''Verify the default value for Opening Size RH, should be "0" '''
        assert "0" == standard_door.check_openingrh_default

    def test_standard_door_022(self, standard_door):
        '''Verify the default value for Opening Size Width, should be "0" '''
        assert "0" == standard_door.check_openingwidth_default

    def test_standard_door_023(self, standard_door):
        '''Verify the default value for SR Left, should be "0" '''
        assert "0" == standard_door.check_srleft_default

    def test_standard_door_024(self, standard_door):
        '''Verify the default value for HR, should be "0" '''
        assert "0" == standard_door.check_hr_default

    def test_standard_door_025(self, standard_door):
        '''Verify the default value for SR Right, should be "0" '''
        assert "0" == standard_door.check_srright_default

    def test_standard_door_026(self, standard_door):
        '''Verify the LHRK dropdown, '''
        assert "FMLHR\nHigh Lift\nVerticle Lift" in standard_door.check_lhrk_list

    def test_standard_door_027(self, standard_door):
        '''Verify each element for Timer/Taper/AdditionalFab details'''
        expected = ('Timber Packers', 'Taper (Max taper 250mm)', 'Additional Fabrication',
                    'Additional Fabrication Required', 'Shop Drawings', 'Lifting/Access Equipment')
        actual = standard_door.check_timber_details
        assert expected == actual,f"Expected:{expected},but got: {actual}"

    def test_standard_door_028(self, standard_door):
        '''Verify each element for all checkboxes'''
        expected = ('Induction Loop',  'Fully Slotted', 'Emergency Key Release','Reverse Colour', 'Battery Backup',
                    'Eco Smart WiFi')
        actual = standard_door.check_checkboxes_details
        assert expected == actual, f"Expected:{expected},but got: {actual}"

    def test_standard_door_029(self, standard_door):
        '''Verify each element for Opener'''
        expected = ('Opener', 'No of Handsets', 'Wall Button', 'Opener Details', 'Digital Keypad',
                    'Internal Push Button','PE Beam','No. of PE Beam Sets')
        actual = standard_door.check_opener_details
        assert expected == actual, f"Expected:{expected},but got: {actual}"

    def test_standard_door_030(self, standard_door):
        '''Verify each element for other elements'''
        expected = ('Weight Being Added', 'Seals', 'Seals 2500mm (QTY)','Seals 3000mm (QTY)','Hang Door From',
                    'Lintel Type', 'Fixing Type','IBeam Noggins', 'Remove and Dispose', 'Job Status',
                    'Expected Delivery Date','Cut Date','Paint Date','QC Date','Other Date')
        actual = standard_door.check_other_details
        assert expected == actual, f"Expected:{expected},but got: {actual}"

    def test_standard_door_031(self, standard_door):
        '''Verify each element for Aditional Infomation'''
        expected = ('Additional Door Information', 'Production Notes   (0 / 50)')
        actual = standard_door.check_additional_details
        assert expected == actual, f"Expected:{expected},but got: {actual}"

    def test_standard_door_032(self, standard_door):
        '''Verify the default options in Door Finish dropdown '''
        assert "Please Select\nSmooth Texture\nTextured\nWoodgrain Texture" == standard_door.check_default_doorfinish


    def test_standard_door_033(self, standard_door):
        '''Verify the Door finish option for Classic door '''
        assert "Please Select\nWoodgrain Texture" == standard_door.check_classic_doorfinish


    def test_standard_door_035(self, standard_door):
        '''Verify the Door finish option for Lincoln door '''
        assert "Please Select\nWoodgrain Texture" == standard_door.check_lincoln_doorfinish


    def test_standard_door_036(self, standard_door):
        '''Verify the Door finish option for Ultraline door '''
        assert "Please Select\nWoodgrain Texture" == standard_door.check_ultraline_doorfinish

    def test_standard_door_037(self, standard_door):
        '''Verify the Door finish option for Wideline door '''
        assert "Please Select\nSmooth Texture\nWoodgrain Texture" == standard_door.check_wideline_doorfinish

    def test_standard_door_038(self, standard_door):
        '''Verify the reverse colour box status for Panel Lift door, should be disabled'''
        assert standard_door.reverse_colour_panel is True

    def test_standard_door_039(self, standard_door):
        '''Verify the Fully Slotted box status for Panel Lift door, should be disabled'''
        assert standard_door.fully_slotted_panel is True

    def test_standard_door_040(self, standard_door):
        '''Verify the Induction Loop box status for Panel Lift door, should be enabled'''
        assert standard_door.induction_loop_panel is True

    def test_standard_door_041(self, standard_door):
        '''Verify the Emergency Key Release box status for Panel Lift door, should be enabled'''
        assert standard_door.emergency_key_panel is True

    def test_standard_door_042(self, standard_door):
        '''Verify the ECO Smart wifi box status for Panel Lift door, should be enabled'''
        assert standard_door.smart_wifi_panel is True

    def test_standard_door_043(self, standard_door):
        '''Verify the Battery Backup box status for Panel Lift door, should be enabled'''
        assert standard_door.battery_backup_panel is True

    def test_standard_door_044(self, standard_door):
        '''Verify the reverse colour box status for Roller door, should be enabled'''
        assert standard_door.reverse_colour_roller is True

    def test_standard_door_045(self, standard_door):
        '''Verify the Fully Slotted box status for Roller door, should be disabled'''
        assert standard_door.fully_slotted_roller is True

    def test_standard_door_046(self, standard_door):
        '''Verify the reverse colour box status for Insulated Sectional door, should be disabled'''
        assert standard_door.reverse_colour_insulated is True

    def test_standard_door_047(self, standard_door):
        '''Verify the Fully Slotted box status for Insulated Sectional door, should be disabled'''
        assert standard_door.fully_slotted_insulated is True

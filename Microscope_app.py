from ScopeFoundry import BaseMicroscopeApp

class OceanOpticsApp(BaseMicroscopeApp):

    # this is the name of the microscope that ScopeFoundry uses 
    # when storing data
    name = 'oceanoptics'
    
    # You must define a setup function that adds all the 
    #capablities of the microscope and sets default settings
    def setup(self):
	
        #Add Hardware components
        from OceanOptics_hardware import OceanOpticsHW
        self.add_hardware(OceanOpticsHW(self))
		
        #Add Measurement components
        from OceanOptics_measurement import OceanOpticsMeasure
        #from PiezoStage_measurement import PiezoStageMeasure
        self.add_measurement(OceanOpticsMeasure(self))
        #self.add_measurement(PiezoStageMeasure(self))
		
        # show ui
        self.ui.show()
        self.ui.activateWindow()


if __name__ == '__main__':
    import sys
    
    app = OceanOpticsApp(sys.argv)
    sys.exit(app.exec_())
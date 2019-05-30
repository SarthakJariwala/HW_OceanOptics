from ScopeFoundry import HardwareComponent
import seabreeze.spectrometers as sb

class OceanOpticsHW(HardwareComponent):
    
    ## Define name of this hardware plug-in
    name = 'oceanoptics_hardware'
    
    def setup(self):
        # Define your hardware settings here.
        # These settings will be displayed in the GUI and auto-saved with data files
        self.settings.New('intg_time', dtype=int, unit='us', initial=3000, vmin=3000)
        self.settings.New('correct_dark_counts', dtype=bool, initial=True)

    def connect(self):
        # Open connection to the device:
        if self.spec is None:
            devices = sb.list_devices()
            self.spec = sb.Spectrometer(devices[0])
            self.ui.status_textBrowser.append("Ocean Optics Device Connected!\n\n Device:\n\n"+str(sb.list_devices()[0]))
        else:
            self.ui.status_textBrowser.append("Already Connected")

        #Connect settings to hardware:
        self.spec.settings.intg_time.connect_to_hardware(
            self.spec.integration_time_micros)

    
        #Take an initial sample of the data.
        self.read_from_hardware()
        
    def disconnect(self):
        #Disconnect the device and remove connections from settings
        self.settings.disconnect_all_from_hardware()
        if self.spec is not None:
            self.spec.close()
            self.ui.status_textBrowser.append("Ocean Optics Device Disconnected")
            del self.spec
            self.spec = None


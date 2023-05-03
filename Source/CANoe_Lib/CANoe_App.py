from Source.CANoe_Lib.CANoe_Measurement import CanoeMeasurement
from Source.CANoe_Lib.CANoe_Configuration import CanoeConfiguration
from Source.CANoe_Lib.CANoe_TestEnvironments import CanoeTestEnvironments
import win32com.client
import os

class CanoeApp:
    """Wrapper class for CANoe Application object"""
    Canoe_config_file_type = ".cfg"
    def __init__(self, canoe_direct_directory:str):
        self.app = win32com.client.Dispatch('CANoe.Application')
        win32com.client.WithEvents(self.app, ApplicationEvent)   
        self.print_canoe_version()
        #load CANoe config with the diretory in the config file
        self.load_canoe_config(cfgPath=canoe_direct_directory)
        #load all COM object
        self.measurement = CanoeMeasurement(self.app.Measurement)
        self.configuration = CanoeConfiguration(self.app.Configuration)
        self.test_environments = CanoeTestEnvironments(self.configuration.test_environments)

    def load_canoe_config(self, cfgPath):
        # current dir must point to the script file
        cfg = os.path.join(os.curdir, cfgPath)
        cfg = os.path.abspath(cfg)
        # check for valid CANoe config file
        if CanoeApp.Canoe_config_file_type not in cfg:
            raise Exception(f"The input CANoe config file is not type '{CanoeApp.Canoe_config_file_type}', please input a valid CANoe config.")
        print('Opening: ', cfg)
        self.app.Open(cfg, True)

    def print_canoe_version(self):
        ver = self.app.Version
        if(ver.major < 15):
            print(f"WARNING: CANoe version < 15 (current version {ver.major}), some function may not work as expected!")
        else:
            print('Loaded CANoe version ', 
                ver.major, '.', 
                ver.minor, '.', 
                ver.Build, '...', sep='')
    def close(self):
        self.app.Quit()
  
#--------------------------- EVENT CALLBACK - START ---------------------------------------------------

class ApplicationEvent:

    def __init__(self):
        pass

    def OnOpen(self, fullname):
        print(f"CANoe app opening '{fullname}'...")

    def OnQuit(self):
        print("CANoe app closing...")

#--------------------------- EVENT CALLBACK - END ---------------------------------------------------

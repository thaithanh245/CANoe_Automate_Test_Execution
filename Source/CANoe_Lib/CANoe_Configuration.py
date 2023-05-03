import win32com.client

class CanoeConfiguration:
    """Wrapper class for CANoe Application object"""
    def __init__(self, configuration_object):
        self.configuration = configuration_object
        win32com.client.WithEvents( self.configuration, ConfigurationEvent)
        self.test_environments = self.configuration.TestSetup.TestEnvironments

#--------------------------- EVENT CALLBACK - START ---------------------------------------------------

class ConfigurationEvent:

    def __init__(self):
        pass

    def OnClose(self):
        print("CANoe configuration closing...")

    def OnSystemVariablesDefinitionChanged(self):
        print("CANoe configuration definition changed...")

#--------------------------- EVENT CALLBACK - END ---------------------------------------------------
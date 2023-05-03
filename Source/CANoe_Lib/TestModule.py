import os
import win32com.client
from A_Event import *

class TestModule:

    Num_test_case_fail = 0
    Started = False
    Stopped = True
    Current_module_name = ""

    def __init__(self, test_module_object):
        self.test_module = test_module_object
        win32com.client.WithEvents(self.test_module, TestModuleEvent)
        self.name = os.path.basename(self.test_module.Path).replace(".xml", "")
        TestModule.Current_module_name = self.name
        self.enable = self.test_module.Enabled

    def execute_all(self):
        self.test_module.ExecuteAll()

    def start(self):
        self.test_module.Start()
        DoEventsUntil(TestModule.Started, f"Start test module '{self.name}'.", 15000)

#--------------------------- EVENT CALLBACK - START ---------------------------------------------------

class TestModuleEvent:

    def __init__(self):
        pass

    def OnPause(self):
        print(f"Test module '{TestModule.Current_module_name}' paused.")

    def OnReportGenerated(self, success, sourceFullName, generatedFullName):
        print(f"Test module '{TestModule.Current_module_name}' report generated")

    def OnStart(self):
        print(f"Test module '{TestModule.Current_module_name}' starting...")
        TestModule.Started = True
        TestModule.Stopped = False

    def OnStop(self, reason):
        print(f"Test module '{TestModule.Current_module_name}' stopped")
        TestModule.Started = False
        TestModule.Stopped = True
        if (int(reason) == 0):
            print("The test module was executed completely.")
        elif (int(reason) == 1):
            print("The test module was stopped by the user.")
        else:
            print("The test module was stopped by measurement stop.")

    def OnVerdictFail(self):
        print("Test case failed!")
        TestModule.Num_test_case_fail += 1

#--------------------------- EVENT CALLBACK - END ---------------------------------------------------
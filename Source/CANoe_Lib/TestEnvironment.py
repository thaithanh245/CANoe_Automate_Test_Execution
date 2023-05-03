from .TestModules import TestModules
from . TestEnvironment_Folders import TestEnvironemntFolders

class TestEnvironment:
    def __init__(self, test_environment_object):
        self.test_environment = test_environment_object
        self.name = self.test_environment.Name
        self.test_environment_status = lambda : self.test_environment.Enabled
        self.test_modules = TestModules(self.test_environment.TestModules)
        self.folders = TestEnvironemntFolders(self.test_environment.Folders)

    def execute_all(self):
        self.test_environment.ExecuteAll()

    def save(self):
        self.test_environment.Save()

    def enable(self):
        self.test_environment.Enabled = True

    def disable(self):
        self.test_environment.Enabled = False
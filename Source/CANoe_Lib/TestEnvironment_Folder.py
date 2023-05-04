from .TestModules import TestModules
from .TestEnvironment_Folders import TestEnvironemntFolders

class TestEnvironmentFolder:
    def __init__(self, test_environemnt_folder_object):
        self.test_environemnt_folder = test_environemnt_folder_object
        self.name = self.test_environemnt_folder.Name
        self.enable = self.test_environemnt_folder.Enabled
        self.test_modules = TestModules(self.test_environemnt_folder.TestModules)
        self.folders = TestEnvironemntFolders(self.test_environemnt_folder.Folders)

    def execute_all(self):
        self.test_environemnt_folder.ExecuteAll()

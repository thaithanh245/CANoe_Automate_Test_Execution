from .TestModules import TestModules

class TestEnvironmentFolder:
    def __init__(self, test_environemnt_folder_object):
        self.test_environemnt_folder = test_environemnt_folder_object
        self.name = self.test_environemnt_folder.Name
        self.enable = self.test_environemnt_folder.Enabled

    def execute_all(self):
        self.test_environemnt_folder.ExecuteAll()

    def get_list_test_modules(self):
        self.test_environemnt_folder.TestModules

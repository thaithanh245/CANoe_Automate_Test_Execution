from TestEnvironment_Folder import TestEnvironmentFolder

class TestEnvironemntFolders:
    def __init__(self, test_environment_folders_object):
        self.test_environment_folders = test_environment_folders_object
        self.num_folder = self.test_environment_folders.Count

    def get_list_of_folders(self) -> list:
        folders_list = []
        
        for folder in range(1, self.num_folder + 1):
            folder_object = TestEnvironmentFolder(self.test_environment_folders.Item(folder))
            folders_list.append(folder_object)

        return folders_list
from .TestEnvironment import TestEnvironment

class CanoeTestEnvironments:
    def __init__(self, test_environments_object):
        self.test_environments = test_environments_object
        self.num_test_environment = self.test_environments.Count

    def get_list_of_test_environments(self) -> list:
        test_environments_list = []
        
        for test_environment in range(1, self.num_test_environment + 1):
            test_environment_object = TestEnvironment(self.test_environments.Item(test_environment))
            test_environments_list.append(test_environment_object)

        return test_environments_list
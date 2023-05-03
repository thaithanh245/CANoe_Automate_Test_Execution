from .TestModule import TestModule

class TestModules:
    def __init__(self, test_module_object):
        self.test_module = test_module_object
        self.num_test_modules = self.test_module.Count

    def get_list_of_test_modules(self) -> list:
        test_modules_list = []
        
        for test_module in range(1, self.num_test_modules + 1):
            test_module_object = TestModule(self.test_module.Item(test_module))
            test_modules_list.append(test_module_object)

        return test_modules_list

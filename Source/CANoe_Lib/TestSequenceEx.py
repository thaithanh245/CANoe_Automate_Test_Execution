import enum
from .TestSequenceItemEx import TestSequenceItemEx
from .A_CANoe_Enum import SequenceItemType

class TestSequenceItemProperties(enum.Enum):
    object = 1
    type = 2
    id = 3
    verdict = 4

class TestSequenceEx:

    def __init__(self, test_sequence_object):
        self.test_sequence = test_sequence_object
        self.num_test_sequence_items = lambda : self.test_sequence.Count

    def get_all_test_sequence_items(self) -> dict:
        test_sequence_items_dict = {}
        
        for test_sequence_item in range(1, self.num_test_sequence_items + 1):
            test_sequence_item_object = TestSequenceItemEx(self.test_sequence.Item(test_sequence_item))
            item_name = test_sequence_item_object.name()
            if item_name not in test_sequence_items_dict.keys():
                test_sequence_items_dict[item_name] = {}
                test_sequence_items_dict[item_name][TestSequenceItemProperties.object.name] = test_sequence_item_object
            else:
                raise Exception("Duplicate test sequence item name (test case name, test group name)!")

            test_sequence_items_dict[item_name][TestSequenceItemProperties.object.type] = test_sequence_item_object.type()
            test_sequence_items_dict[item_name][TestSequenceItemProperties.object.id] = test_sequence_item_object.id()
            test_sequence_items_dict[item_name][TestSequenceItemProperties.object.verdict] = test_sequence_item_object.verdict()

        return test_sequence_items_dict


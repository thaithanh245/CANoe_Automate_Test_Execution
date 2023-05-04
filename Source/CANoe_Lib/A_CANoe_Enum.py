import enum

class SequenceItemType(enum.Enum):
    undefined = 0
    test_case = 1
    test_group= 2

class TestVerdict(enum.Enum):
    not_available = 0
    passed = 1
    failed = 2 
    none = 3
    inconclusive = 4
    error_in_test_system = 5
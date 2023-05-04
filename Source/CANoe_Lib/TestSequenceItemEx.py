
class TestSequenceItemEx:

    def __init__(self, test_sequence_item_object):
        self.test_sequence_item = test_sequence_item_object
        self.name = lambda : self.test_sequence_item.Name
        self.type = lambda : self.test_sequence_item.Type
        self.id = lambda : self.test_sequence_item.Ident
        self.verdict = lambda : self.test_sequence_item.Verdict
        self.status = lambda : self.test_sequence_item.Enabled

    def enable(self):
        self.test_sequence_item.Enabled = True

    def disable(self):
        self.test_sequence_item.Enabled = False


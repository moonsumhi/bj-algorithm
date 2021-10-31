
def merge_two_lists(self, l1, l2):
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwolists(l1.next, l2)
    return l1


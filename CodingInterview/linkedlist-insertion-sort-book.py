from typing import Optional


class ListNode:

    root: Optional["ListNode"] = None

    def __init__(self, val: Optional[int] = None, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def insert(self, val: int) -> None:
        if ListNode.root is None:
            ListNode.root = ListNode(val=val)
            return

        cur_node = ListNode.root
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = ListNode(val=val)

        return

    def __str__(self) -> str:
        cur_node = ListNode.root
        result = f"{cur_node.val}"
        while cur_node.next is not None:
            cur_node = cur_node.next
            result += f", {cur_node.val}"
        return result

    def insertionSortList(self) -> None:
        cur = parent = ListNode(0)
        head = ListNode.root
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            if head and cur.val > head.val:
                cur = parent

        ListNode.root = parent.next


listnode = ListNode()
listnode.insert(-1)
listnode.insert(4)
listnode.insert(2)
listnode.insert(1)
listnode.insert(3)
print(listnode)
listnode.insertionSortList()
print(listnode)

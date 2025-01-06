class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next
def wypisywanie(first):
    current=first
    print(current.val)
    while current.next is not None:
        print(current.next.val)
        current=current.next

class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next
def zad174(first):
    count=0
    while first:
        count+=1
        first=first.next
    return count

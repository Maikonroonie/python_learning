class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next
def reverse(head):
    cur=head
    prev=None
    while cur:
        next_node=cur.next
        cur.next=prev
        prev=cur
        cur=next_node
    return prev

def plsuone(head):
    cur=head
    while cur.val==9:
        cur.val=0
        cur=cur.next
    cur.val=cur.val+1
    return head
def zadanie(head):
    rev=reverse(head)
    plus=plsuone(rev)
    return reverse(plus)

def creator(T):
    head=Node(T[0])
    cur=head
    for i in range(1,len(T)):
        cur.next=Node(T[i])
        cur=cur.next
    return head
def show(head):
    if head==None:
        print()
        return
    print(head.val,end='->')
    return show(head.next)

T1=[1,2,3,4,9,9]
show(creator(T1))
show(zadanie(creator(T1)))


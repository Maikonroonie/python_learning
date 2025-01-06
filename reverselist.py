class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
def reverse(head):
    prev , cur = None, head
    cur_cp=cur
    while cur:
        new_node= cur.next
        cur.next=prev
        prev=cur
        cur=new_node
    return prev
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
T1=[1,2,3,4]
T2=[2,3,4,4,7]
show(creator(T1))
#show(creator(T2))
show(reverse(creator(T1)))

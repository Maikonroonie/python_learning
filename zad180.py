class Node:
    def __init__(self,val, next=None):
        self.val=val
        self.next=next
def zad180(head, a):
    cur=head
    while cur.next:
        cur=cur.next
    cur.next=Node(a)
    return head





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

T1=[1,3,7,4,5,4,2]     
show(creator(T1))
show(zad180(creator(T1), 676))      

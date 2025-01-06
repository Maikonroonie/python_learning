class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next
def delate_every_two(head):
    cur=head
    while cur and cur.next:
        cur.next=cur.next.next
        cur=cur.next
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

T1=[1,3,7,4,5,8,9]     
show(creator(T1))
show(delate_every_two(creator(T1)))   
 

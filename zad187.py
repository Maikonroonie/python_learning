class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
def zadanie187(head):
    cur=head
    cur=cur.next
    prev=cur
    while cur.next:
        while cur.next and cur.val<prev.val:
                prev.next=cur.next
                cur=cur.next
        if cur.next:
            prev=cur
            cur=cur.next
    if cur.val<prev.val:
        prev.next=None
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

T1=[1,2,3,4,3,2,7,3,2,1,6,9,10]
show(creator(T1))
show(zadanie187(creator(T1)))

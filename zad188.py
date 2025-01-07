class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next
def zadanie(head):
    cur=head
    while cur and cur.next:
        if cur.next.val%cur.val==0:
            cur.next=cur.next.next
        else:
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

T1=[5,2,3,4,3,2,7,3,2,1,6,9,10]
show(creator(T1))
show(zadanie(creator(T1)))


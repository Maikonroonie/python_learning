class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next
def append(head,a):
    new_node=Node(a)
    cur=head
    while cur.next!= None:
        cur=cur.next
    cur.next=new_node
def lenght(head):
    count=0
    while head:
        count+=1
        head=head.next
    return count
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
def get(head,idx):
    if idx>=lenght(head):
        print("ERROR index out of range ERROR")
        return None
    cur_idx=0
    cur_val=head
    while True:
        if cur_idx==idx:
            return cur_val.val
        cur_val=cur_val.next
        cur_idx+=1
'''def eraseidx(head, idx):
    if idx>= lenght(head) or idx<0:
        print("ERROR index out of range ERROR")
        return None
    if idx==0:
        return head.next
    cur_idx=0
    cur=head
    while True:
        last=cur
        cur=cur.next
        if cur_idx==idx-1:
            last.next=cur.next
            return head
        cur_idx+=1'''
def eraseidx2(head, idx):
    if idx>=lenght(head):
        print("ERROR index out of range ERROR")
        return None
    if idx==0:
        return head.next
    cur=head
    cur_idx=0
    while True:
        if cur_idx+1==idx:
            cur.next=cur.next.next
            return head
        cur_idx+=1
        cur=cur.next



def eraseval2(head,value):
    while head and head.val==value:
        head=head.next
    cur=head
    while cur and cur.next:
        if cur.next.val==value:
            cur.next=cur.next.next
        else:
            cur=cur.next
    return head
 
T1=[1,2,3,4,2,2]
show(creator(T1))
show(eraseidx2(creator(T1), 5))

            






    




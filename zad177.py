class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
def scaling(head1, head2):
    if head1.val<=head2.val:
        cur=head1
        head1=head1.next
    else:
        cur=head2
        head2=head2.next
    cur_cp=cur
    while head1 and head2:
        if head1.val<=head2.val:
            cur.next=Node(head1.val)
           # cur.next.val=head1.val
            cur=cur.next
            head1=head1.next
        else:
            cur.next=Node(head2.val)
           #cur.next.val=head2.val
            cur=cur.next
            head2=head2.next
    if head1 is None and head2 is None:
        return cur_cp
    if head1 is None:
        while head2:
            cur.next=Node(head2.val)
            #cur.next.val=head2.val
            cur=cur.next
            head2=head2.next 
        return cur_cp 

    if head2 is None:
        while head1:
            cur.next=Node(head1.val)
            #cur.next.val=head1.val
            cur=cur.next
            head1=head1.next
        return cur_cp 
    return cur_cp 




def scaling_rekurwencja(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    if head1.val < head2.val:
        head1.next = scaling_rekurwencja(head1.next, head2)
        return head1
    else:
        head2.next = scaling_rekurwencja(head1, head2.next)
        return head2

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
show(creator(T2))
show(scaling_rekurwencja(creator(T1), creator(T2)))

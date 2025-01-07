class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def zamiana_na_sys3(n):
    if n==0:
        return [0]




def czy_usuwa(a):
    cnt=[0,0,0]
    while a:
        cnt[a%3]+=1
        a//=3
    return cnt[1]>cnt[2]




def zadanie(head):
    while czy_usuwa(head.val):
        head=head.next
    cur=head
    while cur.next:
        if czy_usuwa(cur.next.val):
            cur.next=cur.next.next
        else:
            cur=cur.next
    return head


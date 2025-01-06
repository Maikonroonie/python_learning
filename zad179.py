class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def Zadanie_179(head) -> Node:

    heads = []
    tails = []
    for _ in range(10):  # 10 par podlist do przechowywania lancuchow
        sentinel = Node(0)  # węzeł-wartownik
        heads.append(sentinel)
        tails.append(sentinel)

    while head:
        last_digit = abs(head.val) % 10
        # Odcinamy węzeł od reszty listy i dołączamy do odpowiedniej podlisty
        next_node = head.next
        head.next = None
        tails[last_digit].next = head
        tails[last_digit] = head

        head = next_node

    result_tail = result_sentinel = Node(0)  # wartownik
    for i in range(10):
        if heads[i].next is not None:
            result_tail.next = heads[i].next
            result_tail = tails[i]

    return result_sentinel.next
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

T1=[63636,783873,266,841,150,267,80]     
show(creator(T1))
show(Zadanie_179(creator(T1)))     

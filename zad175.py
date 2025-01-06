class Node:
    def __init__(self, val, next=None):
        self.val=val
        self.next=next
def zawieranie(head, a):
        while head:
            if head.val==a:
                return True
            head=head.next
        return False
def wstawienie(head, a):
    if head is None:
        return Node(a)
    current=head
    while current.next:
        if current.val==a:
            return head
        current=current.next
    current.next=Node(a)
    return head

def creator(T):
    head=Node(T[0])
    cur=head
    for i in range(1,len(T)):
        cur.next=Node(T[i])
        cur=cur.next
    return head
def wypisywanie(first):
    current=first
    print(current.val, end="->")
    while current.next is not None:
        print(current.next.val, end="->")
        current=current.next
def insert(head, value) -> Node:
    return Node(value, head) if not zawieranie(head, value) else head


T1=[1,4,2,1,2,3,4,5,15]
T2=[1552,5,50,5]
head1=creator(T1)
head2=creator(T2)


def usunieciejednego(head, a):
    if head is None:
        return None
    if head.val == a:
        return head.next
    current = head
    while current.next:  # Przechodzimy przez listę
        if current.next.val == a:  # Jeśli znaleźliśmy węzeł do usunięcia
            current.next = current.next.next  # Przekierowujemy wskazanie na kolejny węzeł
            return head  # Zwracamy głowę listy (nie zmienia się)
        current = current.next  # Przechodzimy do kolejnego węzła
    
    return head  # Jeśli wartość nie została znaleziona, zwracamy oryginalną listę
def usuniecieall(head, a):
    if head is None:
        return None
    while head and head.val == a:
        head=head.next
    if not head:
        return None
    current = head
    while current and current.next:  # Przechodzimy przez listę
        if current.next.val == a:  # Jeśli znaleźliśmy węzeł do usunięcia
            current.next = current.next.next  # Przekierowujemy wskazanie na kolejny węzeł
        else: 
            current = current.next  # Przechodzimy do kolejnego węzła
    
    return head  # Jeśli wartość nie została znaleziona, zwracamy oryginalną listę


wypisywanie(head2)
head2=usuniecieall(head2, 5)
wypisywanie(head2)

          

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def set_value(p, n, v) -> Node:
    """podstawiającą  wartość v pod indeks n na lancuchu p"""
    head = Node(None, p)  # wartownik
    prev, current = head, p
    while current and current.val[0] < n:
        prev, current = current, current.next

    if v == None:  #  usuwanie elementu
        if current and current.val[0] == n:
            prev.next = current.next
    elif current and current.val[0] == n:  # Nadpisanie
        current.val = (n, v)
    else:  # Dodanie
        prev.next = Node((n, v), current)

    return head.next  # usuniecie wartownika


def get_value(p, n) -> Node | None:
    """zwracającą wartość elementu o indeksie n,"""
    while p and p.val[0] < n:
        p = p.next
    return p.val[1] if p and p.val[0] == n else None


def initialize_set(p) -> Node:
    """
    Tablica rzadka przechowa tylko wartości  wraz z ich indeksami, np. w postaci listy Przykład:
    Zwykła tablica:
    [None,None,5,None,None,None,8,None,None,3]
    Tablica rzadka
    [(2,5),(6,8),(9,3)]
    """
    head = current = Node(None)  # z wartownikiem
    indeks = 0
    while p:
        if p.val != None:
            current.next = Node((indeks, p.val))
            current = current.next
        p = p.next
        indeks += 1
    return head.next  # bez wartownika

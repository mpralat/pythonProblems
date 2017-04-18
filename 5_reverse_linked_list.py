#https://www.interviewcake.com/question/python/reverse-linked-list
# Given the head of the linked list, reverse it in-place.

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None



def reverse_linked_list(head):
    current_node = head
    next_node = head.next
    previous_node = None

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node

        current_node = next_node

    return previous_node

def print_linked_list(head):
    current_node = head

    while current_node:
        print(current_node.value)
        current_node = current_node.next



if __name__ == "__main__":
    head_node = LinkedListNode(3)
    first_node = LinkedListNode(4)
    second_node = LinkedListNode(5)
    third_node = LinkedListNode(6)
    head_node.next = first_node
    first_node.next = second_node
    second_node.next = third_node

    print_linked_list(head_node)

    reversed_head_node = reverse_linked_list(head_node)

    print_linked_list(reversed_head_node)
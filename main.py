# Программа разворота двусвязного списка
class Node:

    # Создание  узла двусвязного списка
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    # Создание пустого двусвязного списка
    def __init__(self):
        self.head = None

    # Метод разворота двусвязного списка
    def reverse(self):
        temp = None
        current = self.head

        # Пробег по всему двусвязному списку с заменой следующего элемента на предыдущей.
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        # Проверка двусвязного списка на пустоту или одноэлементность
        if temp is not None:
            self.head = temp.prev

    # Наполнение двусвязного списка
    def push(self, new_data):

        new_node = Node(new_data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    # Вывод двусвязного списка
    def printList(self, node):
        while node is not None:
            print (node.data)
            node = node.next


currentList = DoubleLinkedList()
currentList.push(7)
currentList.push(6)
currentList.push(2)
currentList.push(11)

print ("Исходный двусвязный список")
if currentList.printList(currentList.head) != None:
    print (currentList.printList(currentList.head))

currentList.reverse()

print ( "Развернутый двусвязный список")
if currentList.printList(currentList.head) != None:
    print (currentList.printList(currentList.head))


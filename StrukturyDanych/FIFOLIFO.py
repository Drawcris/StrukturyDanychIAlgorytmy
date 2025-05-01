list_fifo = []

list_fifo.append("plant a tree")
list_fifo.append("build a house")
list_fifo.append("have a son")

while len(list_fifo) > 0:
    task = list_fifo.pop(0)
    print(task)

list_lifo = []

list_lifo.append("Blue Box With Glass")
list_lifo.append("Bag with Presents")
list_lifo.append("Barrel of Beer")
list_lifo.append("Cage with a Tiger")

while len(list_lifo) > 0:
    item = list_lifo.pop()
    print(item)
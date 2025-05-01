import queue

my_path='/home/boss/data/projects/bakery/prices.csv'

splited_path = my_path.split('/')
splited_path.remove("")

lifo_queue = queue.LifoQueue()

for element in splited_path:
    lifo_queue.put(element)

while not lifo_queue.empty():
    print(f"getting {lifo_queue.get()}")
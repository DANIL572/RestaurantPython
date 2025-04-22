class Order:
    id = 0 

    def __init__(self, customer_name, dishes=None):
        self.customer_name = customer_name
        self.dishes = dishes if dishes else []
        self.order_id = self.set_id()
        self.status = "новый" 

    @classmethod
    def set_id(cls):
        cls.id += 1
        return cls.id
class RestaurantQueue:
    def __init__(self, queue):
        self.queue = queue

    def is_empty(self):
        return len(self.queue) == 0
    
    def add_order(self, order):
        self.queue.append(order)
        self.status = "новый"
        print(f"Заказ клиента {order.customer_name} добавлен в список заказов, имеет статус {self.status}.")

    def take_order(self):
        if not self.is_empty():
            order = self.queue.pop(0)
            self.status = "в процессе"
            print(f"Заказ клиента {order.customer_name} начал готовиться, имеет статус {self.status}.")
            return order
        else:
            print("Очередь заказов пуста.")

    def complete_order(self, order):
        self.status = "готов"
        print(f"Заказ клиента {order.customer_name}{self.status}.")

    def print_queue(self):
        if self.is_empty():
            print("Очередь заказов пуста.")
        else:
            print("Текущие заказы в очереди:")
            for i, order in enumerate(self.queue):
                print(f"{i + 1}. Заказ клиента {order.customer_name}.")

    def cancel_order(self, order_id):
        for order in self.queue:
            if order.order_id == order_id:
                self.queue.remove(order)
                print(f"Заказ  с ID {order_id} клиента {order.customer_name} отменён.")
                return order
        print(f"Заказ с ID {order_id} не найден.")
            

    def modify_order(self, order_id, new_dishes):
        for order in self.queue:
            if order.order_id == order_id:
                order.dishes = new_dishes
                print(f"Заказ с ID {order_id} клиента {order.customer_name} обновлен. Новые блюда: {new_dishes}")
                return order
        print(f"Заказ с ID {order_id} не найден.")

    def set_priority(self, order_id, priority):
        for order in self.queue:
            if order.order_id == order_id:
                self.queue.remove(order)
                self.queue.insert(max(0, priority), order)
                print(f"Заказ с ID {order_id} клиента {order.customer_name} перемещен на позицию {priority}.")
                return order
        print(f"Заказ c ID {order_id} не найден.")




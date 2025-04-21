class Order:
    def __init__(self, customer_name, order_id):
        self.customer_name = customer_name
        self.dishes = []
        self.order_id = order_id
        
class RestaurantQueue:
    def __init__(self, queue):
        self.queue = queue

    def is_empty(self):
        return len(self.queue) == 0
    
    def add_order(self, order):
        self.queue.append(order)
        status = "новый"
        print(f"Заказ клиента {order.customer_name} добавлен в список заказов, имеет статус {status}.")

    def take_order(self):
        if not self.is_empty():
            order = self.queue.pop(0)
            status = "в процессе"
            print(f"Заказ клиента {order.customer_name} начал готовиться, имеет статус {status}.")
            return order
        else:
            print("Очередь заказов пуста.")

    def complete_order(self, order):
        status = "готов"
        print(f"Заказ клиента {order.customer_name}{status}.")

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
                order.priority = priority
                print(f"Приоритет заказа с ID {order_id} клиента {order.customer_name} установлен на {priority}.")
                return order.priority
        print(f"Заказ с ID {order_id} не найден.")


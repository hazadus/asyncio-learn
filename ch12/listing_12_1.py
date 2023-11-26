"""
Очередь в супермаркете
"""
import asyncio
from asyncio import Queue
from random import randrange
from typing import List


class Product:
    def __init__(self, name: str, checkout_time: float):
        self.name = name
        self.checkout_time = checkout_time


class Customer:
    def __init__(self, customer_id, products: List[Product]):
        self.customer_id = customer_id
        self.products = products


async def checkout_customer(queue: Queue, cashier_number: int):
    while not queue.empty():
        customer: Customer = queue.get_nowait()
        print(f"Cashier {cashier_number} serving customer {customer.customer_id}...")
        for product in customer.products:
            print(
                f"Cashier {cashier_number} serving customer {customer.customer_id}: {product.name}"
            )
            await asyncio.sleep(product.checkout_time)
        print(f"Cashier {cashier_number} done serving customer {customer.customer_id}.")
        # NB: call `task_done()` for each `queue.get_nowait()` call!
        queue.task_done()


async def main():
    customer_queue = Queue()

    all_products = [
        Product("Beer", 2),
        Product("Bananas", 0.5),
        Product("Sausages", 0.2),
        Product("Toilet paper", 0.2),
        Product("Milk", 0.4),
    ]

    for i in range(10):
        products = [
            all_products[randrange(len(all_products))] for _ in range(randrange(10))
        ]
        customer_queue.put_nowait(Customer(i, products))

    cashiers = [
        asyncio.create_task(checkout_customer(customer_queue, j)) for j in range(3)
    ]

    # NB: don't forget to gather `customer_queue.join()`!
    await asyncio.gather(
        customer_queue.join(),
        *cashiers,
    )


asyncio.run(main())

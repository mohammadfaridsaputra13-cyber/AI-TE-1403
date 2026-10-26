
import math


class Agent:
    def __init__(self, agent_id):
        self.agent_id = agent_id

    def communicate(self, message):
        print(f"[{self.agent_id}] {message}")


class DeliveryAgent(Agent):
    def __init__(self, agent_id, x, y, capacity):
        super().__init__(agent_id)
        self.x = x
        self.y = y
        self.capacity = capacity
        self.completed = 0

    def calculate_distance(self, destination):
        return math.sqrt(
            (self.x - destination[0]) ** 2
            + (self.y - destination[1]) ** 2
        )

    def is_available(self):
        return self.capacity > 0

    def deliver(self, order):
        if not self.is_available():
            self.communicate("Kapasitas habis!")
            return False

        self.communicate(
            f"Mengirim pesanan {order['id']}"
        )

        self.x, self.y = order["destination"]
        self.capacity -= 1
        self.completed += 1

        self.communicate(
            f"Pesanan {order['id']} selesai."
        )
        return True


class MonitoringAgent(Agent):
    def __init__(self, agent_id):
        super().__init__(agent_id)
        self.history = []

    def record(self, order_id, delivery_agent):
        self.history.append({
            "order": order_id,
            "agent": delivery_agent.agent_id
        })

        self.communicate(
            f"Mencatat pesanan {order_id}"
        )

    def show_report(self):
        print("\n=== LAPORAN PENGIRIMAN ===")

        for record in self.history:
            print(
                f"Pesanan {record['order']} "
                f"dikirim oleh {record['agent']}"
            )

        print(f"Total selesai: {len(self.history)}")


class CoordinatorAgent(Agent):
    def __init__(self, agent_id, delivery_agents, monitor):
        super().__init__(agent_id)
        self.delivery_agents = delivery_agents
        self.monitor = monitor

    def assign_order(self, order):
        self.communicate(
            f"Menerima pesanan {order['id']}"
        )

        available_agents = [
            agent for agent in self.delivery_agents
            if agent.is_available()
        ]

        if not available_agents:
            self.communicate(
                "Tidak ada kurir tersedia!"
            )
            return

        best_agent = min(
            available_agents,
            key=lambda agent: agent.calculate_distance(
                order["destination"]
            )
        )

        self.communicate(
            f"Menugaskan {best_agent.agent_id}"
        )

        success = best_agent.deliver(order)

        if success:
            self.monitor.record(
                order["id"], best_agent
            )



def main():
    delivery_agents = [
        DeliveryAgent("Kurir-A", 0, 0, 2),
        DeliveryAgent("Kurir-B", 5, 5, 2),
        DeliveryAgent("Kurir-C", 10, 10, 2)
    ]

    monitor = MonitoringAgent("Monitor-1")

    coordinator = CoordinatorAgent(
        "Coordinator-1",
        delivery_agents,
        monitor
    )

    orders = [
        {"id": "P001", "destination": (2, 3)},
        {"id": "P002", "destination": (8, 9)},
        {"id": "P003", "destination": (4, 4)},
        {"id": "P004", "destination": (9, 10)},
        {"id": "P005", "destination": (1, 1)}
    ]

    print("=== MULTI-AGENT DELIVERY SYSTEM ===")

    for order in orders:
        print("\n-------------------------")
        coordinator.assign_order(order)

    monitor.show_report()

    print("\n=== STATUS AKHIR AGENT ===")
    for agent in delivery_agents:
        print(
            f"{agent.agent_id} | "
            f"Posisi: ({agent.x}, {agent.y}) | "
            f"Sisa kapasitas: {agent.capacity} | "
            f"Selesai: {agent.completed}"
        )


if __name__ == "__main__":
    main()


class NodeCommunicator:
    """Handles communication between decentralized nodes."""

    def __init__(self):
        self.node_status = "disconnected"

    def initialize_node(self):
        """Simulates initialization of a node in the decentralized network."""
        self.node_status = "connected"
        print("Node successfully connected to the network.")
    
    def send_message(self, message):
        """Simulates sending a message to another node."""
        print(f"Sending message: {message}")
        return "message_sent"
    
    def receive_message(self):
        """Simulates receiving a message from another node."""
        print("Message received.")
        return "message_received"

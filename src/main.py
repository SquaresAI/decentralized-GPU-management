import os
from gpu_management.gpu_allocation import allocate_gpu_resources
from gpu_management.node_communication import NodeCommunicator

def main():
    """Entry point for the decentralized GPU management system."""
    print("Initializing Decentralized GPU Management System...")
    
    # Initialize Node Communicator
    node_communicator = NodeCommunicator()
    node_communicator.initialize_node()
    
    # Allocate GPU Resources
    allocation_result = allocate_gpu_resources()
    print("GPU Allocation Result:", allocation_result)

if __name__ == "__main__":
    main()

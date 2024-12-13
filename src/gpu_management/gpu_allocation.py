
import random

def allocate_gpu_resources():
    """Simulates GPU resource allocation for decentralized nodes."""
    available_gpus = random.randint(1, 10)
    allocated_gpus = min(available_gpus, random.randint(1, 5))
    
    return {
        "available_gpus": available_gpus,
        "allocated_gpus": allocated_gpus,
        "status": "success" if allocated_gpus > 0 else "failure"
    }

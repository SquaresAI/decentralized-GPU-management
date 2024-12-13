
# Decentralized GPU Management

This module manages GPU resources across decentralized nodes while integrating blockchain-based incentivization mechanisms for contributing nodes. The system allows efficient allocation, fault tolerance, and monitoring of distributed GPU resources.

## Features

- **Decentralized GPU Allocation**: Dynamically allocates GPU resources based on node capacity and task requirements.
- **Blockchain Incentivization**: Tracks contributions using Ethereum smart contracts and rewards contributors.
- **Fault Tolerance**: Implements failover mechanisms for uninterrupted operations.
- **Scalability**: Supports adding or removing nodes dynamically in the network.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/SquaresAI/decentralized-GPU-management.git
   cd decentralized-GPU-management
   ```

2. **Build the Docker Image**:
   ```bash
   docker-compose build
   ```

3. **Start the Service**:
   ```bash
   docker-compose up
   ```

4. **Verify GPU Nodes**:
   Use the following command to list available GPU devices:
   ```bash
   docker exec -it <container_id> nvidia-smi
   ```

## Configuration

The node's configuration file is located at `config/node_config.yaml`. Customize it according to your setup:

```yaml
node:
  id: "node-001"
  capacity:
    gpu_count: 2
  blockchain:
    wallet_address: "0xYourEthereumWalletAddress"
    private_key: "YourPrivateKey"
```

## Testing

Run the included test suite to validate the setup:

```bash
python3 -m unittest discover tests
```

## Contributing

Contributions are welcome! Submit a pull request or create an issue if you encounter any problems.

## License

This project is licensed under the MIT License.

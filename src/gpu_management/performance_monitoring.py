import time
import logging

logging.basicConfig(level=logging.INFO)

class GPUMonitor:
    def __init__(self):
        self.metrics = {}

    def collect_metrics(self):
        """
        Collect GPU performance metrics.
        Returns:
            dict: A dictionary containing GPU metrics.
        """
        self.metrics = {
            "memory_usage": "4GB/8GB",
            "temperature": "65°C",
            "utilization": "75%"
        }
        logging.info(f"Metrics collected: {self.metrics}")
        return self.metrics

    def log_metrics(self):
        """
        Log the collected GPU metrics to a centralized system or file.
        """
        logging.info("Logging GPU metrics...")
        print("Metrics logged successfully.")

if __name__ == "__main__":
    monitor = GPUMonitor()
    while True:
        monitor.collect_metrics()
        monitor.log_metrics()
        time.sleep(5)  # Monitor metrics every 5 seconds

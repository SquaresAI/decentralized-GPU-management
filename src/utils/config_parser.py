import yaml
import json

class ConfigParser:
    """Class for parsing and validating configuration files."""

    def __init__(self, config_path):
        self.config_path = config_path
        self.config_data = None

    def load_config(self):
        """Loads the configuration file based on its extension."""
        if self.config_path.endswith('.yaml') or self.config_path.endswith('.yml'):
            self.config_data = self._load_yaml()
        elif self.config_path.endswith('.json'):
            self.config_data = self._load_json()
        else:
            raise ValueError("Unsupported configuration file format. Use YAML or JSON.")
        return self.config_data

    def _load_yaml(self):
        """Private method to load YAML configuration files."""
        try:
            with open(self.config_path, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            raise ValueError(f"Error loading YAML configuration: {e}")

    def _load_json(self):
        """Private method to load JSON configuration files."""
        try:
            with open(self.config_path, 'r') as file:
                return json.load(file)
        except Exception as e:
            raise ValueError(f"Error loading JSON configuration: {e}")

    def validate_config(self, required_keys):
        """Validates the loaded configuration file against required keys."""
        if not self.config_data:
            raise ValueError("Configuration data is not loaded. Call `load_config` first.")
        missing_keys = [key for key in required_keys if key not in self.config_data]
        if missing_keys:
            raise ValueError(f"Missing required configuration keys: {missing_keys}")
        return True

# Example usage
if __name__ == "__main__":
    config = ConfigParser("config.yaml")
    data = config.load_config()
    config.validate_config(["gpu_node_id", "resource_limits"])
    print("Configuration is valid.")

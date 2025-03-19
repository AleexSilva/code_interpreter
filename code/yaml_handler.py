import os
import yaml
from typing import Any

class YAMLHandler:
    def __init__(self, filename: str, input_dir: str = "../input"):
        self.filepath = os.path.join(input_dir, filename)
        
    def read_yaml(self) -> dict:
        """Reads the YAML file and returns its contents with correct types."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"YAML file not found: {self.filepath}")
        
        with open(self.filepath, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file) or {}
        
        return self._process_data(data)

    def _process_data(self, data: Any) -> Any:
        """Processes YAML data to correctly identify types."""
        if isinstance(data, dict):
            return {key: self._process_data(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [self._process_data(item) for item in data]
        elif isinstance(data, str) and "{{" in data and "}}" in data:
            return data  # Keep as string with variable placeholder
        return data
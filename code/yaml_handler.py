import os
import yaml

class YAMLHandler:
    def __init__(self, filename: str, input_dir: str = "../yaml_files"):
        self.filepath = os.path.join(input_dir, filename)
        
    def read_yaml(self) -> dict:
        """Reads the YAML file and returns its contents as a dictionary."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"YAML file not found: {self.filepath}")
        
        with open(self.filepath, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file) or {}

    def write_yaml(self, data: dict) -> None:
        """Writes the given dictionary to the YAML file."""
        with open(self.filepath, 'w', encoding='utf-8') as file:
            yaml.safe_dump(data, file, default_flow_style=False, allow_unicode=True)

    def update_yaml(self, new_data: dict) -> None:
        """Updates the YAML file by merging new data with existing contents."""
        data = self.read_yaml()
        data.update(new_data)
        self.write_yaml(data)
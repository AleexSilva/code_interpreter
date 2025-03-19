from yaml_handler import YAMLHandler

def main():
    # Initialize the YAML handler for 'input.yaml'
    yaml_handler = YAMLHandler("input.yaml")
    
    # Read the YAML file
    yaml_data = yaml_handler.read_yaml()
    
    # Extract the 'system_prompt' variable if it exists
    system_prompt = yaml_data.get("system_prompt")
    
    print(f"system_prompt: {system_prompt}")

if __name__ == "__main__":
    main()
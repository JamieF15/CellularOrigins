from robot import robot
import json
from jsonschema import validate, ValidationError

ROBOT_CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "robot_commands": {
            "type": "array",
            "items": {
                "oneOf": [
                    {
                        "type": "object",
                        "properties": {
                            "PLACE": {
                                "type": "object",
                                "properties": {
                                    "x": {
                                        "type": "string",
                                        "pattern": "^[0-5]$"
                                    },
                                    "y": {
                                        "type": "string",
                                        "pattern": "^[0-5]$"
                                    },
                                    "direction": {
                                        "type": "string",
                                        "enum": ["NORTH", "EAST", "SOUTH", "WEST"]
                                    }
                                },
                                "required": ["x", "y", "direction"]
                            }
                        },
                        "required": ["PLACE"]
                    },
                    {
                        "type": "string",
                        "enum": ["MOVE", "LEFT", "RIGHT", "REPORT"]
                    }
                ]
            }
        }
    },
    "required": ["robot_commands"]
}

def validate_config(config):
    try:
        validate(instance=config, schema=ROBOT_CONFIG_SCHEMA)
        return True
    except ValidationError as e:
        print(f"Configuration validation error: {e.message}")
        return False

def start():
    try:
        with open('robot_config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Error: robot_config.json not found.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON in robot_config.json.")
        return

    if not validate_config(config):
        print("Invalid configuration. Exiting.")
        return

    process_movement_commands(config.get("robot_commands", []))

def process_movement_commands(commands):
    robot_instance = None
    for command in commands:
        if isinstance(command, dict) and "PLACE" in command:
            place_info = command["PLACE"]
            x = int(place_info["x"])
            y = int(place_info["y"])
            direction = place_info["direction"]
            robot_instance = robot(x, y, direction)
        elif robot_instance:
            robot_instance.invoke_movement_commands([command])

if __name__ == "__main__":
    start()

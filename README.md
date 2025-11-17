# Toy Robot Simulator

A simple command-driven Toy Robot Simulator written in Python.  
The robot moves on a 5x5 grid based on commands defined in a JSON file.

---

## How to Run

### 1. Install Dependencies
Make sure you have Python 3 installed. Then install the required package:

```bash
pip install jsonschema
```

### 2. Configuration File
The script reads the file robot_config.json, which can be edited.
The file is validated against a schema to ensure the command is correct.

### 3. Running the Simulator
Run the main script:

```bash 
python main.py
```

With the included configuration file, the output should be:
```3, 3, NORTH```

### 4. Running Unit Tests
Run the test suite with either unittest or pytest:


## Using unittest
```python -m unittest tests.py -v```

## Or using pytest (if installed)
```pytest tests.py```

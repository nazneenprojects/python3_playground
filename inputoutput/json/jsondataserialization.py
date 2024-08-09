import json
import pickle

# Sample data to be serialized
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "has_children": False,
    "hobbies": ["reading", "travelling", "swimming"]
}

# Convert the Python object to a JSON string
json_data = json.dumps(data)

# Pickle the JSON string
with open('data.pkl', 'wb') as f:
    pickle.dump(json_data, f)

# Unpickle the JSON string from the file
with open('data.pkl', 'rb') as f:
    json_data = pickle.load(f)

# Convert the JSON string back to a Python object
data_loaded = json.loads(json_data)

# Print the loaded data
print("Loaded data:")
print(data_loaded)

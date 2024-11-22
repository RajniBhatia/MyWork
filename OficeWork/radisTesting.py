import redis

# Connect to Redis server
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Store data
r.set("name", "Alice")
r.set("age", "30")
r.set("Designation","Software Enginer")
# Retrieve data
name = r.get("name")
age = r.get("age")
Designation=r.get("Designation")

print(f"Name: {name}, Age: {age}, Designation: {Designation}")

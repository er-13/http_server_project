import requests

# GET
print(requests.get("http://127.0.0.1:5000/users").json())

# POST
print(requests.post("http://127.0.0.1:5000/users", json={"id":3, "name":"Charlie"}).json())

# PUT
print(requests.put("http://127.0.0.1:5000/users/3", json={"name":"Charles"}).json())

# DELETE
print(requests.delete("http://127.0.0.1:5000/users/3").json())
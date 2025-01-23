from method import load_file, save_file, delete_file

data= load_file("data/user.json")
print(data)
data.append({
    "name":"twst test"
})
save_file("data/user.json", data)

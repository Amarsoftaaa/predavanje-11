import json

with open ("data/user.json", "r") as file:
    data = json.load(file)
    data.append({
        "name":"Elvira Huremovic",
        "age" : 55,
        "height" : 170,
        "gender" : "feMale",
    })


    print(data)

    with open ("data/user.json", "w") as file:
        json.dump(data, file, indent=4)
from flask import Flask, request, Response
import json

app=Flask(__name__)
menu=[
    {"id": 1, "name": "Espresso", "price": 120},
    {"id": 2, "name": "Cappuccino", "price": 150}
]

def json_data(data, status=200):
    return Response(json.dumps(data), status=status, mimetype="application/json")

@app.route("/")
def home():
    return json_data({"message": "Welcome to the Coffee Shop API"})

@app.route("/api/coffee", methods=["GET"])
def get_all_coffee():
    return json_data(menu)

#single coffee y id
@app.route("/api/coffees/<int:item_id>", methods=["GET"])
def get_coffee(item_id):
    for item in menu:
        if item["id"]==item_id:
            return json_data(item)
    return json_data({"error": "not found coffee"}, status=404)

#add coffee
@app.route("/api/coffees", methods=["POST"])
def add_coffee():
    data=request.get_json()
    if not data or not data.get("name") or not data.get("price"):
        return json_data({"error": "invalid data"}, status=400)
    
    new_id= menu[-1]["id"]+1 if menu else 1
    new_item={
        "id": new_id,
        "name": data["name"],
        "price": data["price"]
        }
    menu.append(new_item)
    save_menu()
    return json_data(new_item, status=201)


#update cofee
@app.route("/api/coffees/<int:item_id>", methods=["PUT"])
def update_coffee(item_id):
    data=request.get_json()

    for item in menu:
        if item["id"]==item_id:
            item["name"]=data.get("name", item["name"])
            item["price"]=data.get("price", item["price"])
            save_menu()
            return json_data(item)
    return json_data({"error": "coffee item not found"}, status=404)
            
#delete coffee
@app.route("/api/coffees/<int:item_id>", methods=["DELETE"])
def del_coffee(item_id):
    for item in menu:
        if item["id"]==item_id:
            menu.remove(item)
            save_menu()
            return json_data("coffe item deleted")
    return json_data({"message": "coffee item deleted"})

def save_menu():
    with open("menu.json", "w") as file:
        json.dump(menu, file)

if __name__ == '__main__':
    app.run(debug=True)
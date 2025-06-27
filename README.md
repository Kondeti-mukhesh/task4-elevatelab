Firstly, I created a simple REST API using Python and Flask to manage a coffee menu (like in a coffee shop).

I added a list of coffee items with id, name, and price to simulate the menu.

The API supports CRUD operations:

GET /api/coffees – To fetch all coffees.

POST /api/coffees – To add a new coffee (with application/json).

PUT /api/coffees/<id> – To update a coffee item by ID.

DELETE /api/coffees/<id> – To remove a coffee item by ID.

All responses are returned in JSON format using json.dumps() and Response.

I tested API endpoints using curl from the command line (e.g., curl -X POST -H "Content-Type: application/json"...).

Finally, this code was completely written and tested by me for learning and practice purposes.

Pizza Restaurant API Documentation


This API provides endpoints to manage relationships between restaurants and pizzas. It allows you to create, retrieve, update, and delete restaurants and their associated pizzas.

Setup
To set up this API, follow these steps:

Clone the repository.
Install dependencies by running npm install.
Set up your database and configure the connection in config/database.js.
Run migrations to create necessary tables by executing npm run migrate.
Models
Restaurant
Attributes:
name (String, required, unique, max length: 50): The name of the restaurant.
address (String): The address of the restaurant.
Pizza
Attributes:
name (String, required): The name of the pizza.
ingredients (String): The ingredients used in the pizza.
RestaurantPizza
Attributes:
price (Number, required, range: 1-30): The price of the pizza at the restaurant.
Validations
RestaurantPizza

Must have a price between 1 and 30.
Restaurant

Must have a name less than 50 characters in length.
Must have a unique name.
Routes


GET /restaurants
Returns a list of restaurants.
Response format:

[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5th Avenue"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
]


GET /restaurants/:id
Returns details of a specific restaurant along with its pizzas.
Response format:

{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}

If the restaurant is not found:


{
  "error": "Restaurant not found"
}


DELETE /restaurants/:id
Deletes a restaurant and its associated restaurant pizzas.
Response: [].

If the restaurant is not found:

{
  "error": "Restaurant not found"
}


GET /pizzas
Returns a list of pizzas.
Response format:

[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]


POST /restaurant_pizzas
Creates a new association between a pizza and a restaurant.
Request body format:

{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}


If successful, returns the details of the associated pizza.
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}


If there are validation errors:
{
  "errors": ["validation errors"]
}
Note
Ensure to handle errors appropriately and provide meaningful error messages for better usability.
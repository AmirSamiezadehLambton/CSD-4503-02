from pymongo import MongoClient  # pip install pymongo

# MongoDB Atlas Client
client = MongoClient("mongodb+srv://root:dBAxAFAZS3t43anh@cluster0.ktsh8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

app_db = client.app  # app is the name of the database in MongoDB Atlas
products_collection = app_db.products  # products is the name of the collection inside the database


# Example product objects
products = [
    # {
    #     "name": "Product 1",
    #     "image": "/static/images/product1.jpg",
    #     "price": 29.99,
    #     "tag": "New"
    # },
    # {
    #     "name": "Product 2",
    #     "image": "/static/images/product2.jpg",
    #     "price": 49.99,
    #     "tag": "Discounted"
    # },
    # {
    #     "name": "Product 3",
    #     "image": "/static/images/product3.jpg",
    #     "price": 19.99,
    #     "tag": "Best Seller"
    # }
    # {
    #     "name": "Product 4",
    #     "image": "/static/images/product4.jpg",
    #     "price": 9.99,
    #     "tag": "Black Friday"
    # },
    {
        "name": "Product 5",
        "image": "/static/images/product5.jpg",
        "price": 69.99,
        "tag": "Black Friday"
    }
]

# Insert the products into MongoDB
products_collection.insert_many(products)





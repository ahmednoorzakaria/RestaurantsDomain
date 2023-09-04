from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review
from faker import Faker
import random

# Create a database engine
engine = create_engine("sqlite:///restuarant_domain.db")

# Create tables if they don't exist

# Create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Create a Faker instance
faker = Faker()

# Remove existing data
session.query(Customer).delete()
session.query(Restaurant).delete()
session.query(Review).delete()

# Create a list of restaurants
restaurants = []
for _ in range(10):
    restaurant = Restaurant(
        name=faker.name(),
        price=faker.random_int(min=1, max=5),
    )
    restaurants.append(restaurant)
    session.add(restaurant)

# Create a list of customers
customers = []
for _ in range(10):
    customer = Customer(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
    )
    customers.append(customer)
    session.add(customer)

# Commit the customers and restaurants to ensure they have IDs
session.commit()

# Create a list of reviews
for _ in range(10):
    review = Review(
        star_rating=faker.random_int(min=1, max=5),
        restaurant_id=random.choice(restaurants).id,  # Choose a random restaurant
        customer_id=random.choice(customers).id,  # Choose a random customer
    )

    session.add(review)

# Commit the changes to the database
session.commit()

# Close the session
session.close()

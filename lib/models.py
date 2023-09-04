from sqlalchemy import create_engine, ForeignKey, Table, Column, Integer, String
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from faker import Faker

Base = declarative_base()

class Restaurant(Base):
    """
    The Restaurant class represents a table in a database that stores information about restaurants.
    It is used in conjunction with the Review class to establish a relationship between restaurants and customer reviews.
    """

    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Define the relationship with Review
    reviews = relationship("Review", back_populates="restaurant")

    # Define the association_proxy to access customers through reviews
    customers = association_proxy("reviews", "customer")

    def __repr__(self):
        return f'Restaurant(id={self.id}, name={self.name})'

class Customer(Base):
    """
    The `Customer` class represents a customer in a restaurant review system.
    It is a SQLAlchemy model that is mapped to the "customers" table in the database.
    This class has a one-to-many relationship with the `Review` class, allowing a customer to have multiple reviews.
    It also has an association proxy to access the associated restaurants through the reviews.
    """

    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define the relationship with Review
    reviews = relationship("Review", back_populates="customer")

    # Define the association_proxy to access restaurants through the reviews
    restaurants = association_proxy("reviews", "restaurant")

    def __repr__(self):
        """
        Returns a string representation of the customer object.
        """
        return f"Customer(id={self.id}, name={self.first_name} {self.last_name})"

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer(), primary_key=True)

    star_rating = Column(Integer())
    restaurant_id = Column(Integer(), ForeignKey("restaurants.id"))
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    # Define the relationship with Restaurant
    restaurant = relationship("Restaurant", back_populates="reviews")

    # Define the relationship with Customer
    customer = relationship("Customer", back_populates="reviews")

    def __repr__(self):
        return f'Review(id={self.id}, Rating={self.star_rating}, Restaurant={self.restaurant_id}, Customer={self.customer_id})'

if __name__ == "__main__":
    engine = create_engine("sqlite:///restaurant_domain.db")
    Base.metadata.create_all(engine)

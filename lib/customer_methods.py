def customer_reviews(customer):
    """
    Returns a collection of all the reviews that the Customer has left.
    """
    return customer.reviews

def customer_restaurants(customer):
    """
    Returns a collection of all the restaurants that the Customer has reviewed.
    """
    return customer.restaurants

def customer_full_name(customer):
    """
    Returns the full name of the customer, with the first name and the last name concatenated, Western style.
    """
    return f"{customer.first_name} {customer.last_name}"

def customer_favorite_restaurant(customer):
    """
    Returns the restaurant instance that has the highest star rating from this customer.
    """
    reviews = customer.reviews
    if not reviews:
        return None
    favorite_review = max(reviews, key=lambda r: r.star_rating)
    return favorite_review.restaurant

def customer_add_review(customer, restaurant, rating):
    """
    Takes a restaurant (an instance of the Restaurant class) and a rating,
    creates a new review for the restaurant with the given restaurant_id.
    """
    new_review = Review(star_rating=rating, restaurant=restaurant, customer=customer)
    session.add(new_review)
    session.commit()

def customer_delete_reviews(customer, restaurant):
    """
    Takes a restaurant (an instance of the Restaurant class) and
    removes all their reviews for this restaurant.
    """
    reviews_to_delete = [review for review in customer.reviews if review.restaurant == restaurant]
    for review in reviews_to_delete:
        session.delete(review)
    session.commit()

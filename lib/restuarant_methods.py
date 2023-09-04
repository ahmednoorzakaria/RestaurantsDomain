def restaurant_reviews(restaurant):
    """
    Returns a collection of all the reviews for the restaurant.
    """
    return restaurant.reviews

def restaurant_customers(restaurant):
    """
    Returns a collection of all the customers who reviewed the restaurant.
    """
    return restaurant.customers

def restaurant_fanciest(cls):
    """
    Returns one restaurant instance for the restaurant that has the highest price.
    """
    return cls.query.order_by(cls.price.desc()).first()

def restaurant_all_reviews(restaurant):
    """
    Returns a list of strings with all the reviews for this restaurant formatted as follows:
    [
        "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
        "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
    ]
    """
    reviews = restaurant.reviews
    formatted_reviews = []
    for review in reviews:
        formatted_review = f"Review for {restaurant.name} by {review.customer.full_name()}: {review.star_rating} stars."
        formatted_reviews.append(formatted_review)
    return formatted_reviews

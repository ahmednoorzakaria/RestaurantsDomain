def review_customer(review):
    """
    Returns the Customer instance for this review.
    """
    return review.customer

def review_restaurant(review):
    """
    Returns the Restaurant instance for this review.
    """
    return review.restaurant

def review_full_review(review):
    """
    Returns a string formatted as:
    Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.
    """
    return f"Review for {review.restaurant.name} by {review.customer.full_name()}: {review.star_rating} stars."

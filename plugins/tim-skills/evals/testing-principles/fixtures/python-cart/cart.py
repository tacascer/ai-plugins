# Requirement: free shipping at subtotal >= 50.
def total(subtotal):
    shipping = 0 if subtotal > 50 else 5
    return subtotal + shipping

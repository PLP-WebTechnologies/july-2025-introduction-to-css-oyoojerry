# Question                         1
def calculate_discount(price, discount_percent):
    """
    This function calculates the final price after applying a discount.
    If the discount is less than 20%, the function returns the original price.
    
    Parameters:
    price (float or int): The original price of the item.
    discount_percent (float or int): The discount percentage to apply.
    
    Returns:
    float: The final price after applying the discount (if applicable).
    """

    # Check if the discount percentage is 20 or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price

        # Subtract the discount amount from the original price
        final_price = price - discount_amount

        # Return the discounted final price
        return final_price
    else:
        # If discount is less than 20%, return the original price unchanged
        return price


# Example usage of the function:

# Case 1: Discount is 25% (greater than or equal to 20%)
# This should apply the discount
print(calculate_discount(1000, 25))  # Output: 750.0

# Case 2: Discount is 10% (less than 20%)
# This should return the original price
print(calculate_discount(1000, 10))  # Output: 1000




# Question                           2
# Define the function to calculate discount
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is less than 20%, returns the original price.
    """
    if discount_percent >= 20:  # Check if discount is 20% or higher
        discount_amount = (discount_percent / 100) * price  # Calculate discount amount
        final_price = price - discount_amount  # Subtract discount from original price
        return final_price  # Return the discounted price
    else:
        return price  # If discount is less than 20%, return original price unchanged


# Prompt the user to enter the original price of the item
price = float(input("Enter the original price of the item: "))

# Prompt the user to enter the discount percentage
discount_percent = float(input("Enter the discount percentage: "))

# Call the function to calculate the final price
final_price = calculate_discount(price, discount_percent)

# Check if a discount was applied
if discount_percent >= 20:
    # Print the discounted price if discount was applied
    print(f"The final price after {discount_percent}% discount is: {final_price} - calculate_discount.py:70")
else:
    # Print the original price if no discount was applied
    print(f"No discount applied. The original price is: {final_price} - calculate_discount.py:73")

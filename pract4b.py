# Get the probability values from the user
while True:
    try:
        P_A = float(input("Enter the probability of event A (0 to 1): "))
        if 0 <= P_A <= 1:
            break # Valid input, exit the loop
        else:
            print("Probability must be between 0 and 1. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid probability between 0 and 1.")
while True:
    try:
        P_B = float(input("Enter the probability of event B (0 to 1): "))
        if 0 <= P_B <= 1:
            break # Valid input, exit the loop
        else:
            print("Probability must be between 0 and 1. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid probability between 0 and 1.")

# Calculate joint probability P(A and B)
P_A_and_B = P_A * P_B
# Format the result to two decimal places
formatted_result = "{:.2f}".format(P_A_and_B)
# Print the result
print("P(A and B) =", formatted_result)

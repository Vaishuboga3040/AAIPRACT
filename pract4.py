def get_valid_probability_input(prompt):
    while True:
        try:
            probability = float(input(prompt))
            if 0 <= probability <= 1:
                return probability # Valid input, return the probability
            else:
                print("Probability must be between 0 and 1. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid probability between 0 and 1.")

# Get the probability values from the user
P_B = get_valid_probability_input("Enter the probability of event B (0 to 1): ")

P_A_and_B = get_valid_probability_input("Enter the probability of events A and B (0 to 1): ")

# Calculate conditional probability P(A|B)
P_A_given_B = P_A_and_B / P_B

# Check if the calculated conditional probability is greater than 1
if P_A_given_B > 1:
    print("Inconsistent result. Please check the inputs again.")
else:
    # Format the result to two decimal places
    formatted_result = "{:.2f}".format(P_A_given_B)
    print("P(A|B) =", formatted_result)


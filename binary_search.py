def binary_search(min_limit, max_limit, count=0):
    middle = (min_limit + max_limit) // 2
    question = input(f"I think your number it's: {middle}. Is this your number or no?\n"
                     f" if yes - enter yes, if not - enter lower or upper:\n ").lower()
    if question == "yes":
        return f"Your number found by {count} times!"
    elif question == "upper":
        count += 1
        return binary_search(middle, max_limit, count)
    elif question == "lower":
        count += 1
        return binary_search(min_limit, middle, count)

min_limit = int(input("Enter lower limit:\n "))
max_limit = int(input("Enter upper limit:\n "))
print(binary_search(min_limit, max_limit))
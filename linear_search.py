def locate_card(cards, query):
    """Taking the list of cards and the item to find the card (Query) as input and
    returning the position of the element on the list"""
    # Create a new position variable with the value 0
    position = 0
    # Loop to run until it reaches to the end of the list of cards
    while position <= len(cards):
        # Checking if the position is past the last element and return -1
        if position == len(cards):
            return -1
        # Checking if the card at the position is the same as the query and return position
        elif cards[position] == query:
            return position
        # Increment the position by 1
        position += 1


def evaluate_tests(test_cases):
    """Accepts all the test and edge cases as input and compare them with the desired output"""
    # Create two elements for number of test and passed tests
    number_of_test = 0
    passed_test = 0
    # Loop over all the test and edge cases already added to the list
    for tests in test_cases:
        # call locate_card and catch the value in result parameter
        result = locate_card(**tests['input'])
        print(
            f"Test case #{number_of_test}\nInput\n{tests['input']}\nexpected output:\n{tests['output']}\nactual output:\n{result}")
        # Check if the result is equal to the desired output and print test passed and increase the value of passed_test
        if result == tests['output']:
            print("Test passed")
            passed_test += 1
        # else printing case failed
        else:
            print(f"Test case {number_of_test} failed")

        number_of_test += 1


# The generic test case in which the query card is somewhere in the middle of the list
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7,
    },
    'output': 3
}

# A blank tests list to later append all the test cases including edge cases
tests_list = []

tests_list.append(test)

# Query at the front of the list
tests_list.append({'input': {
    'cards': [13, 10, 7, 4, 3, 2, 1, 0],
    'query': 13},
    'output': 0})

# Query at the end of the list
tests_list.append({'input': {
    'cards': [13, 10, 7, 4, 3, 2, 1, 0],
    'query': 0},
    'output': 7})

# One element in the list which is the query
tests_list.append({'input': {
    'cards': [13],
    'query': 13},
    'output': 0})

# The list is empty
tests_list.append({'input': {
    'cards': [],
    'query': 13},
    'output': -1})

# Query is not in the list
tests_list.append({'input': {
    'cards': [13, 10, 7, 4, 3, 2, 1, 0],
    'query': 5},
    'output': -1})

# Query occurs once in the list with repeated cards
tests_list.append({'input': {
    'cards': [13, 13, 13, 11, 10, 10, 6, 3, 3, 2],
    'query': 6},
    'output': 6})

# Repeated occurrence of query in the single list
tests_list.append({'input': {
    'cards': [13, 13, 7, 4, 4, 3, 3, 3, 1, 0],
    'query': 3},
    'output': 5})

# Call the evaluate test function to test all the edge cases
evaluate_tests(tests_list)

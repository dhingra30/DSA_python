def test_location(cards, query, mid):
    """Accepts cards, query and mid returns the side of the list containing the element if not found"""
    # Checking if the card at the middle is the query
    if cards[mid] == query:
        # checking if the card before the middle is the query (multiple occurrence)
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        # if not then the first occurrence of the card is found
        else:
            return 'found'
    # if the card at the middle is greater than the query then the query exists on the right side of the list
    elif cards[mid] > query:
        return 'right'
    # else the query exists on the left of the list
    else:
        return 'left'


def locate_card(cards, query):
    """Accepts cards list and query and returns the position of the card or -1 if not found"""
    # defining the start and end parameters to point to the beginning and end of the list
    start, end = 0, len(cards) - 1
    while start <= end:
        # finding the middle element of the list
        mid = (start + end) // 2
        # comparing if the card at the middle position is the query and returning the position of the middle card
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        # checking if the query is smaller than the card at the middle position and discarding the starting half of
        # the list
        elif result == 'right':
            start = mid + 1
        # checking if the query is higher than the cards at the middle position and discarding the later half of the
        # list
        elif result == 'left':
            end = mid - 1
    return -1


def evaluate_tests(test_cases):
    """Accepts all the test and edge cases as input and compare them with the desired output"""
    # Create two elements for number of test and passed tests
    number_of_test = 1
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
        print(f"{passed_test} tests passed out of {number_of_test-1} tests")


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

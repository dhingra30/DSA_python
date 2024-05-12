from linear_search import evaluate_tests, tests_list


def locate_cards(cards, query):
    """Accepts cards list and query and returns the position of the card or -1 if not found"""
    # defining the start and end parameters to point to the beginning and end of the list
    start, end = 0, len(cards) - 1
    while start != end:
        # finding the middle element of the list
        mid = (start + end) // 2
        # comparing if the card at the middle position is the query and returning the position of the middle card
        if cards[mid] == query:
            return mid
        # checking if the query is smaller than the card at the middle position and discarding the starting half of
        # the list
        elif cards[mid] > query:
            start = mid + 1
        # checking if the query is higher than the cards at the middle position and discarding the later half of the
        # list
        elif cards[mid] < query:
            end = mid - 1
    return -1


evaluate_tests(tests_list)

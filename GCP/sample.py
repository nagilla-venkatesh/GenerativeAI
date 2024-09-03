def title_case(string, minor_words=''):
    string = string.lower().split()
    minor_words = minor_words.lower().split()
    for i in range(len(string)):
        if i == 0 or string[i] not in minor_words:
            string[i] = string[i].capitalize()
    return ' '.join(string)

def test_title_case():  
    assert title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings'
    assert title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows'
    assert title_case('the quick brown fox') == 'The Quick Brown Fox'
    print('All test cases pass')


test_title_case()

def multiplication_table(n):
    return [[i*j for j in range(1, n+1)] for i in range(1, n+1)]

def test_multiplication_table():
    assert multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    assert multiplication_table(5) == [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
    print('All test cases pass')


# Write a pysaprk code to calculate teh running total 
# of sales in a store. 

# Input:
# sales = [(1, 100), (2, 200), (3, 300), (4, 400)]
# Output:
# [(1, 100), (2, 300), (3, 600), (4, 1000)]

def running_total(sales):
    total = 0
    result = []
    for i in sales:
        total += i[1]
        result.append((i[0], total))
    return result
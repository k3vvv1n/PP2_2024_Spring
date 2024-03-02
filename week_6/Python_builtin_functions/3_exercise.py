def determine(test_num, test):
    rev_test = ''.join(reversed(test))
    print('Test #{} is {}a palindrome'.format(test_num, '' if rev_test == test else 'not '))


determine(1, input())
determine(2, input())
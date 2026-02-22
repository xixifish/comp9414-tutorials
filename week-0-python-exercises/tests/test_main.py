from main import BankAccount, if_3_2, is_palindrome, loops_3_1, while_3_1


def test_prime_numbers():
    primes = loops_3_1()
    assert 2 in primes
    assert 3 in primes
    assert 4 not in primes
    assert 997 in primes  # largest prime under 1000


def test_digit_count():
    assert while_3_1(12345) == 5
    assert while_3_1(1) == 1
    assert while_3_1(1000) == 4


def test_ticket_price():
    assert if_3_2(2, False) == 0  # toddler, free
    assert if_3_2(8, False) == 10  # child
    assert if_3_2(25, False) == 20  # adult
    assert if_3_2(25, True) == 16  # adult with membership (20% off)


def test_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True


def test_bank_account():
    account = BankAccount("123", 100)
    account.deposit(50)
    assert account.balance == 150
    account.withdrawal(30)
    assert account.balance == 120

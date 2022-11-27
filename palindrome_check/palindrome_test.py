from palindrome import palindrome_check

def test_palindrome():
    assert palindrome_check("racecar") == "It's a palindrome!"
    assert palindrome_check("lopol") == "It's a palindrome!"
    assert palindrome_check("deed") == "It's a palindrome!"
    assert palindrome_check("mallam") == "It's a palindrome!"
    assert palindrome_check("panda") == "This string is not a palindrome"
    assert palindrome_check("donkey") == "This string is not a palindrome"




if __name__ == "__main__":
    test_palindrome()
    print("Everything passed :)")
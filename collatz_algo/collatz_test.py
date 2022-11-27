from collatz import collatz_algo

def test_collatz():
    assert collatz_algo(-42) == "The number has to be greater than 1"
    assert collatz_algo(0) == "The number has to be greater than 1"
    assert collatz_algo(5) == 5
    assert collatz_algo(123) == 46
    assert collatz_algo(42) == 8




if __name__ == "__main__":
    test_collatz()
    print("Everything passed :)")
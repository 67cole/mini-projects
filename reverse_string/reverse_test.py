from reverse import reverse_string

def test_reverse():
    assert reverse_string("dictionary") == "yranoitcid"
    assert reverse_string("hello") == "olleh"
    assert reverse_string("12345") == "54321"
    assert reverse_string("!@#") == "#@!"


if __name__ == "__main__":
    test_reverse()
    print("Everything passed :)")



from pi_generator import pi_to_dec

def test_pi():
    assert pi_to_dec(3) == "3.141"
    assert pi_to_dec(0) == "3"
    assert pi_to_dec(-10) == "You've entered a number smaller than 0. This is invalid!"
    assert pi_to_dec(17) == "Sorry! This program only offers up to 15 decimal places."



if __name__ == "__main__":
    test_pi()
    print("Everything passed :)")



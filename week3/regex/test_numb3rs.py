from numb3rs import validate

def test_valid_formats():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_invalid_ranges():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("256.0.0.0") == False
    assert validate("0.256.0.0") == False

def test_invalid_strings_and_lengths():
    assert validate("cat") == False
    assert validate("127.0.0") == False  # Too short
    assert validate("127.0.0.1.5") == False  # Too long
    assert validate("127.0..1") == False # Missing number

def test_leading_zeros():
    assert validate("192.168.001.1") == False
    assert validate("01.0.0.0") == False
    assert validate("00.0.0.0") == False
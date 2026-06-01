import pytest
from working import convert

def test_valid_times():
    # Standard times
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    
    # Night shifts / reverse times
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    
    # 12 AM / 12 PM edge cases
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_invalid_formats():
    # Using a dash instead of "to"
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        
    # Extra unexpected characters
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
        
    # Missing spaces
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

def test_invalid_bounds():
    # Minutes too high
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
        
    # Hours too high/low for 12-hour clock
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("0:00 AM to 5:00 PM")
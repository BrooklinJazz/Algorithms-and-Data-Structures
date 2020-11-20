def time_conversion(s):
    clock = s[-2:]
    time = s[:-2]                                                     
    h = int(time[:2])                             
    if (h == 12 and clock == "AM"):
        h = "00"
        time = h + time[2:]          
    elif (h == 12 and clock == "PM"):
        h = "12"
        time = h + time[2:]                                        
    elif (clock == "PM"):                                                      
        h = h + 12
        time = str(h) + time[2:]
    return time

def test_PM_case():
    assert time_conversion("05:42:00PM") == "17:42:00"

def test_AM_case():
    assert time_conversion("05:42:00AM") == "05:42:00"

def test_morning_case():
    assert time_conversion("12:00:00AM") == "00:00:00"

def test_midnight_case():
    assert time_conversion("12:00:00PM") == "12:00:00"

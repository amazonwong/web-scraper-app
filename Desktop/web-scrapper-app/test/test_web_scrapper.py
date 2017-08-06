from app.web_scrapper import enlarge

def test_enlarge():  
    result = enlarge(3)
    assert result == 300

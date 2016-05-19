def test_app__Schaukasten__1(browser):
    res = browser.get('/api/')
    assert {'success': 'You have asked localhost:80 and got the answer'
            ' 84/2.'} == res.json

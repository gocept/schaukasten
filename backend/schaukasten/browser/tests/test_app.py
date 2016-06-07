def test_app__Schaukasten__1(browser):
    res = browser.get('/api/')
    assert {'success': 'You are using the schaukasten api version 0.1.',
            'version': 0.1} == res.json

"""This module contains the API tests for the schaukasten."""
import schaukasten.file


def test_app__Schaukasten__api__1(browser):
    """It returns the current api version."""
    res = browser.get('/api/')
    assert {'msg': 'You are using the schaukasten api version 0.1.',
            'status': 'success',
            'version': 0.1} == res.json


def test_app__Schaukasten__add_file__1(browser):
    """It returns an error if no sufficient json is sent."""
    res = browser.post_json('/api/files', {})
    assert set([('status', 'error')]) <= set(res.json.items())


def test_app__Schaukasten__add_file__2(browser):
    """It returns an error if wrong json is sent."""
    res = browser.post_json('/api/files', dict(file_input=dict()))
    assert set([('status', 'error')]) <= set(res.json.items())


def test_app__Schaukasten__add_file__3(browser, database):
    """It returns a success if a file was uploaded and saved."""
    res = browser.post_json(
        '/api/files',
        dict(file_input=dict(filename='my_test.txt', file="My test text")))
    assert set([('status', 'success')]) <= set(res.json.items())
    assert schaukasten.file.File.get(res.json['file'])

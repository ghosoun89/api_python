import pytest
import requests
from pytest_bdd import scenarios, given, then, parsers

UNIVERSITY_API = 'http://universities.hipolabs.com/search'

CONVERTERS={
    'country': str,
    'university': str
}

@pytest.fixture
def api_response():
    return UNIVERSITY_API

scenarios('../features/api.feature')

@given(parsers.parse('search for specific "{university}"'), target_fixture='university_res')
@given(parsers.parse('search for university using part of university name "{university}"'), target_fixture='university_res')
def university_res(api_response, university):
    response = requests.get(f'{api_response}?name={university}')
    return response

@then(parsers.parse('the response status code is "{code:d}"'))
def response_code(university_res,code):
    assert university_res.status_code == code

@then(parsers.parse('all the returned universities have "{part}" in their names'))
def response_contents(university_res, part):
    res_body = university_res.json()
    for obj in res_body:
        assert part in obj["name"] 

@then(parsers.parse('the response contains results for "{university}"'))
def response_contents(university_res, university):
    name_response = university_res.json()[0]['name']
    assert name_response == university

@given(parsers.parse('search for university using specific country name "{country}" and "{university}" university'), target_fixture='university_county_res')
def university_county_res(api_response, university, country):
    response = requests.get(f'{api_response}?name={university}&country={country}')
    return response

@then(parsers.parse('the response has status code "{code:d}"'))
def response_code(university_county_res,code):
    assert university_county_res.status_code == code

@then(parsers.parse('all the result has country name "{country}"'))
def response_contents(university_county_res, country):
    res_body = university_county_res.json()
    for obj in res_body:
        assert country in obj['country']

@then(parsers.parse('all the returned universities contain "{part}" in their names'))
def response_contents(university_county_res, part):
    res_body = university_county_res.json()
    for obj in res_body:
        assert part in obj["name"]

@given(parsers.parse('searching for university without using the filters'), target_fixture='search_res')
def search_res(api_response):
    response = requests.get(api_response)
    return response

@then(parsers.parse('the response status code "{code:d}"'))
def response_code(search_res,code):
    assert search_res.status_code == code

@then(parsers.parse('the result length is greater than "{length:d}"'))
def response_length(search_res, length):
    assert len(search_res.json()) > length

@given(parsers.parse('search using invalid {country} name'), converters=CONVERTERS, target_fixture='search_invalid_country')
def search_invalid_country(api_response, country):
    response = requests.get(f'{api_response}?country={country}')
    return response

@then('the response body should be empty')
def check_body(search_invalid_country):
    assert len(search_invalid_country.json()) == 0

@given(parsers.parse('Search using valid country "{country}" but non-existing university name "{university}"'),target_fixture='search_country_university')
@given(parsers.parse('using valid university "{university}" but non-existing country name "{country}"'))
def search_country_university(api_response, university, country):
    response = requests.get(f'{api_response}?name={university}&country={country}')
    return response

@then('the response body is empty')
def check_body(search_country_university):
    assert len(search_country_university.json()) == 0



















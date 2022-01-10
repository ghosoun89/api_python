import requests
import json

apiUrl = "http://universities.hipolabs.com/search"

def test_search_by_name():
    response = requests.get(apiUrl+"?name=Campion College")
    res_body = response.json()
    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 200
    assert len(res_body) == 1
    for obj in res_body:
        assert obj['name'] == "Campion College"

def test_search_by_part_name():
    response = requests.get(apiUrl+"?name=Saint")
    res_body = response.json()
    assert response.status_code == 200
    for obj in res_body:
        assert "Saint" in obj["name"]


def test_search_by_country_and_part_name():
    response = requests.get(apiUrl+"?country=Canada&name=Brand")
    res_body = response.json()
    assert response.status_code == 200
    for obj in res_body:
        assert obj["country"] == "Canada"
        assert "Brand" in obj["name"]

def test_list_universities():
    response = requests.get(apiUrl)
    res_body = response.json()
    assert response.status_code == 200
    assert len(res_body) > 0

def test_search_by_numbers():
    response = requests.get(apiUrl+"?country=123")
    assert len(response.json()) == 0

def test_search_non_existing_country():
    response = requests.get(apiUrl+"?country=test")
    assert len(response.json()) == 0

def test_search_by_valid_university_non_existing_country():
    response = requests.get(apiUrl+"?country=test&name=Campion College")
    assert len(response.json()) == 0

def test_search_by_valid_country_non_existing_university():
    response = requests.get(apiUrl+"?country=Canada&name=test")
    assert len(response.json()) == 0

def test_search_by_arabic():
    response = requests.get(apiUrl+"?country=الاردن")
    assert len(response.json()) == 0

def test_search_by_part_country():
    response = requests.get(apiUrl+"?country=United")
    assert len(response.json()) == 0

# f = open('/home/test/Desktop/api_python/tests/data.json')
# data = json.load(f)
# print(type(data))
#     # print (i)
#     # print(i['description'])
# def test_search_with_invalid_params():
#     for i in data:
#         f"""[summary]
#         {i['description']}
#         """

#         print('anything', i)
#         print(i['description'])
#         response = requests.get(apiUrl + i['params'])
#         assert len(response.json()) == 0
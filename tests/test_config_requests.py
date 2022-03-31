import requests

def test_get_config():
	response = requests.get("http://polo.chiton:8080/diematic/config")
	assert response.status_code == 200

def test_get_config_content_type():
	response = requests.get("http://polo.chiton:8080/diematic/config")
	assert response.headers['Content-Type'] == 'application/json'

def test_get_config_content_length():
	response = requests.get("http://polo.chiton:8080/diematic/config")
	assert  int(response.headers['Content-Length']) > 0

def test_get_config_content():
	response = requests.get("http://polo.chiton:8080/diematic/config")
	length = int(response.headers['Content-Length'])
	assert len(response.content) == length

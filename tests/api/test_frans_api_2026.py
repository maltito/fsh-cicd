from unicodedata import name
import requests
from src.frans_api_helper import create_student
from src.frans_api_helper import delete_a_student
base_url_original = "https://test-379574553568.us-central1.run.app/student"
base_url = "https://test-379574553568.us-central1.run.app/"
API_KEY = "malte-testar-2026"
def test_get_all_students():
   headers = {"API_KEY": API_KEY}
   response = requests.get(base_url_original, headers=headers)
   
   assert response.status_code == 200


def test_create_a_student():
   headers = {"API_KEY": API_KEY}

   new_student = create_student(name="Lars", age=22, grade="VG")

   response = requests.post(base_url + "/student", headers=headers, json=new_student)
   assert response.status_code == 200
   assert response.json()["status"] == "OK"


def test_get_a_student():
   headers = {"API_KEY": API_KEY}

   student = create_student(name="Anna", age=30, grade="G")
   create_response = requests.post(base_url + "/student", headers=headers, json=student)
   id = create_response.json()["id"]

   response = requests.get(base_url + "/student/" + str(id), headers=headers)
   
   assert response.status_code == 200

   
def test_delete_a_student():
    
    response = delete_a_student(12)
    
    assert response.status_code == 200



def test_update_a_student():
   #Arrange
    headers = {"API_KEY": API_KEY}  
    id = create_student(name="test_update_student", age=56, grade="VG")
    updated_student = {"name": "test_update_student", "age": 56, "grade": "IG"}
   
   #Act
    response = requests.put(base_url + "/student/" + str(id), headers=headers, json=updated_student)

   #Assert
    assert response.status_code == 200






   






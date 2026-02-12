import requests

base_url_original = "https://test-379574553568.us-central1.run.app/student"
base_url = "https://test-379574553568.us-central1.run.app/"
API_KEY = "malte-testar-2026"

def create_student(name, age, grade):
      input = {"name": name,
               "age": age,
               "grade": grade
               }
      headers = {"API_KEY": API_KEY}
      response = requests.post(base_url + "/student", headers=headers,json=input)
      print("Created student with name: ", input["name"])

      return response.json().get("student_id")

def delete_a_student(id):
    headers = {"API_KEY": API_KEY}  
    
    response = requests.delete(base_url + "/student/" + str(id), headers=headers)
    
    return response

def update_a_student(id, name, age, grade):
    input = {"name": name,
             "age": age,
             "grade": grade
             }
    
    headers = {"API_KEY": API_KEY}
    
    response = requests.put(base_url + "/student/" + str(id), headers=headers,json=input)
    
    return response


def get_a_student(id):
    headers = {"API_KEY": API_KEY}
    
    response = requests.get(base_url + "/student/" + str(id), headers=headers)
    
    print("Fetched student with id: ", id)
    
    return response.json() 

def get_all_students():
    headers = {"API_KEY": API_KEY}
    
    response = requests.get(base_url_original, headers=headers)
    
    print("Fetched all students")
    
    return response.json()
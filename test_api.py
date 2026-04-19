import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "age": 18,
    "gender": "male",
    "school_type": "public",
    "parent_education": "graduate",
    "study_hours": 5,
    "attendance_percentage": 85,
    "internet_access": "yes",
    "travel_time": "<15 min",
    "extra_activities": "yes",
    "study_method": "notes",
    "math_score": 70,
    "science_score": 75,
    "english_score": 80
}

res = requests.post(url, json=data)
print(res.json())
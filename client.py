import requests 
BASE_URL = "http://localhost:8000" 

def fetch_llm_1(model, topic):
    url = f"{BASE_URL}/{model}/tech/invoke" 
    try:
        response = requests.post(url, json= {'input': {'topic': topic}})
        if response.status_code == 200:
            try:
                data = response.json() 
                print(f"\n{model.capitalize()} Tech Response: \n{data['output']['content']}")
            except requests.exceptions.JSONDecodeError:
                print(f"\n Error: Received empty or invalid json response  from {model}. Response text:\n{response.text}") 
    except requests.exceptions.RequestException as e :
        print(f"\n Request Error: Could not connect to {model} API. \n{e}") 


def fetch_llm_2(model, topic):
    url = f"{BASE_URL}/{model}/nontech/invoke" 
    try:
        response = requests.post(url, json= {'input': {'topic': topic}})
        if response.status_code == 200:
            try:
                data = response.json() 
                print(f"\n{model.capitalize()} Tech Response: \n{data['output']['content']}")
            except requests.exceptions.JSONDecodeError:
                print(f"\n Error: Received empty or invalid json response  from {model}. Response text:\n{response.text}") 
    except requests.exceptions.RequestException as e :
        print(f"\n Request Error: Could not connect to {model} API. \n{e}") 

fetch_llm_1("gemini" , "What is Python?")
fetch_llm_2("groq", "What is 2+2*3 ?") 
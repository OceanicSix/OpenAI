import requests
import pyperclip

def makeReq(api_key,role,prompt):
    api_endpoint = "https://api.openai.com/v1/chat/completions"
    api_key = api_key

    #Set HTTP request

    proxies={"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

    headers={
        "Content-Type": "application/json",
        "Authorization": f'Bearer {api_key}'
    }

    post_data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": role
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0
    }

    http_resp = requests.post(api_endpoint, json=post_data, headers=headers)

    if http_resp.status_code == 200:
        chat_resp = http_resp.json()
        result = chat_resp["choices"][0]["message"]["content"]
        print(f"Chatgpt: {result}")
        # copy result to clipboard
        pyperclip.copy(result)
    else:
        result=http_resp.json()
    return result
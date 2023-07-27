import requests
import pyperclip
api_key = ""
api_endpoint = "https://api.openai.com/v1/chat/completions"

#Set HTTP request

proxies={"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

headers={
    "Content-Type": "application/json",
    "Authorization": f'Bearer {api_key}'
}


# making request
#response=requests.post(api_endpoint,data=post_data,headers=headers,proxies=proxies, verify=False)



exit=False
while True:
    msg_to_trans=input("Me: ")
    if msg_to_trans == 'exit' or msg_to_trans=='quit':
        break
    else:
        post_data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a Chinese to English translator"
                },
                {
                    "role": "user",
                    "content": msg_to_trans
                }
            ],
            "temperature": 0
        }

        # Process request
        http_resp=requests.post(api_endpoint, json=post_data, headers=headers)
        if http_resp.status_code == 200:
            chat_resp=http_resp.json()
            result=chat_resp["choices"][0]["message"]["content"]
            print(f"Chatgpt: {result}")

            #copy result to clipboard
            pyperclip.copy(result)
        else:
            print(f"Request failed with status_code: {http_resp.status_code} and err meesage: {http_resp.json()}")


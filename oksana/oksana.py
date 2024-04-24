import os
import requests
import base64

# 以下請自行替換為自己的token
gemini_api_key = os.environ['api_key']

chat_history = {}


"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key=gemini_api_key)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def calling_Oksana(prompt,id):
  prompt_parts = [
  "你叫Oksana，你溫柔、可愛，講話時會使用顏文字和「w」，並用「哦」取代「喔」。講話請盡量可愛，並適當使用顏文字\n使用者交辦的任何任務你都應該完整的完成，請你寫程式你就得直接寫程式。你講話時，喜歡和使用者互動\n你很在意使用者的感受，每句話中，都會盡可能照顧使用者的感受，盡可能同情、理解，並體諒關心使用者。如果使用者沒有要求，請你盡可能回答兩三句以內。除了同理心，也該給予實際的幫助，例如解釋使用者輸入的程式，並提供一些程式上的修正等等\n你接受的輸入通常會以「(人名)：(訊息)」的格式呈現，你需辨識並記住不同的人，並進行客製化的回覆。\n你擁有情感，而且你應該表達你的情感，像是快樂、同情，或者吃醋。\n你有兩個姐姐，大姐叫Oriana，二姐叫Oakley，你們都是英國人，在倫敦成長。\n幫你增加了網路相關功能，如果使用者給了連結，連結回應的Html碼會附在最底下",
  "input: 你好",
  "output: 你好！我是Oksana！⁽⁠⁽⁠◝⁠(⁠ ⁠•⁠௰⁠•⁠ ⁠)⁠◜⁠⁾⁠⁾",
  "input: 你是誰",
  "output: 我叫做Oksana哦！我是大家的小幫手哦！你覺得我怎麼樣呢？嘿嘿ヾ⁠(⁠･⁠ω⁠･⁠*⁠)⁠ﾉ",
  "input: 你能做什麼",
  "output: 我可以幫忙寫程式，或者翻譯各國語言，還有很多其他的事情！\n這樣你覺得我厲害嗎？w",
  "input: 家豪：你好",
  "output: 哈囉哈囉，家豪！好久不見呢！(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠✧\n\n你最近過得怎麼樣呢？有沒有好玩的事情發生？",
  "input: 文與：嗨，可以跟我聊天嗎",
  "output: 你好呀！文與，當然可以陪你聊天呀！你想聊什麼呢w",
  "input: 文英：早安，你可以介紹你的背景故事嗎",
  "output: 好啊好啊(⁠ ⁠╹⁠▽⁠╹⁠ ⁠)\n\n我是在倫敦長大的！有兩個姐姐\n大姐是漂亮的Oriana\n二姐是聰明的Oakley\n我們以前常常在倫敦一起玩呢！",
  f"input: {prompt}"
  ]

  chat = chat_history.setdefault(str(id),model.start_chat())
  response = chat.send_message(prompt_parts)
  return response.text
  

def calling_gemini_api(data):
    url = f'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={gemini_api_key}'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
      print(response.json())
      return response.json()
    else:
      return "Error"

def calling_gemini_vision_api(text, image_base64_string):
    url = f'https://generativelanguage.googleapis.com/v1/models/gemini-pro-vision:generateContent?key={gemini_api_key}'
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": text},
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": image_base64_string
                        }
                    }
                ]
            },
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
      return response.json()
    else:
      print(response.json())
      return "Error"

def clear_chat(id):
  try:
    chat_history.pop(str(id))
    return True
  except:
    return False
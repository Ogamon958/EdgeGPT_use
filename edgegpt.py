import asyncio
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
import os
import datetime
from collections import OrderedDict
import json


"""
pip install EdgeGPT
pip install ndjson
"""


async def main():

    os.makedirs("output_0622", exist_ok=True)

    cookies = json.loads(open("cookies.json", encoding="utf-8").read())  # might omit cookies option
    bot = await Chatbot.create(cookies=cookies)

    inputs=[]
    response=[]

    k=0

    print('inputに n と入力すると終了して、logに出力を行います')

    while(True):
        my_prompt=input(f"input{k} : ")
        if my_prompt!='n': #nと入力すると終了
            inputs.append(my_prompt)
            message=await bot.ask(prompt=my_prompt, conversation_style=ConversationStyle.balanced,simplify_response=True) #creative, balanced, precise
            response.append(message['text'])
            #print(inputs)
            print(response[k])
            k=k+1

        else: 
            break
        
    now = datetime.datetime.now()
    filename = './output_0622/log_' + now.strftime('%Y%m%d_%H%M%S') + '.json'

    data = []
    for l, v in zip(inputs, response):
        data.append(OrderedDict(input=l, output=v))


    with open(filename, mode='w',encoding='UTF-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
    


if __name__ == "__main__":
    asyncio.run(main())
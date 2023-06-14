import asyncio
from EdgeGPT import Chatbot, ConversationStyle

import json

import ndjson #インストール必要


"""
pip install EdgeGPT
pip install ndjson
"""


async def main():
    
    my_prompt=input("input : ")

    

    bot = await Chatbot.create() # Passing cookies is optional
    message=await bot.ask(prompt=my_prompt, conversation_style=ConversationStyle.creative)
    await bot.close()
    


    #そのままの出力
    with open('log/raw_test_input.ndjson', 'a',encoding="utf-8") as f:
        writer = ndjson.writer(f,ensure_ascii=False)
        writer.writerow(message)



    #input (prompt) とoutput (bingAIの回答) のみの出力
    response=message['item']['messages'][1]['text']
    print(response)
    d = dict(input=my_prompt, output=response)
    with open('log/test_input.ndjson', 'a',encoding="utf-8") as f:
        writer = ndjson.writer(f,ensure_ascii=False)
        writer.writerow(d)


    #標準出力させる
    print(d)
    


if __name__ == "__main__":
    asyncio.run(main())
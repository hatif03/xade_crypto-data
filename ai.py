from openai import OpenAI, ChatCompletion
from api import call_api
import os


function_descriptions = [
            {
                "name": "get_crypto_data",
                "description": "Get financial data for trading by given coin name",
                "parameters": {
                    "type": "string",
                    "properties": {
                        "coin_name": {
                            "type": "string",
                            "description": "The name of the coin we need details about.",
                        },
                    },
                    "required": ["coin_name"],
                },
            }
        ]

def get_ai_response(user_query):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4-0613",

        # This is the chat message from the user
        messages=[{"role": "user", "content": user_query}],

        functions=function_descriptions,
        function_call="auto",
    )

    ai_response_message = response["choices"][0]["message"]
    print(ai_response_message)

    coin_name = eval(ai_response_message['function_call']['arguments']).get("coin_name")

    function_response = call_api(url=f"https://api.coingecko.com/api/v3/coins/{coin_name}", params={"localization":False})
    print(function_response)

    second_response = ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "user", "content": user_query},
            ai_response_message,
            {
                "role": "function",
                "name": "get_coin_details",
                "content": function_response,
            },
        ],
    )

    return second_response['choices'][0]['message']['content']
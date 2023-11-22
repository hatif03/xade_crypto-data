from flask import Flask, jsonify, request
from api import call_api
from ai import get_ai_response

app = Flask(__name__)

app.config["SECRET_KEY"] = "xade-crypto-ai"


@app.route("/get-all-data", methods=["GET"])
def get_all_data():
    data = call_api(url="https://api.coingecko.com/api/v3/coins/markets", params={"vs_currency": "inr", "per_page": 250})
    if data:
        return data
    else:
        return jsonify({"message": "Failed to retrieve data from api"})

@app.route("/data/coin/<id>", methods=["GET"])
def get_data_by_id(id):
    if id:
        data = call_api(url=f"https://api.coingecko.com/api/v3/coins/{id}", params={"localization":False})
        if data:
            return data
        else:
            return jsonify({"message": "Failed to retrieve data from api"})

    return jsonify({"message": "Failed"})

@app.route("/chat", methods=["GET"])
def ai_chat():
    user_query = request.args.get("query")
    response = get_ai_response(user_query)
    return user_query



if __name__ == "__main__":
    app.run(debug=True)






#import flask for api and openAI for GPT clone 
from flask import Flask, request, jsonify,json
from openai import OpenAI
from apikey import OPENAI_API
app = Flask(__name__)


key=OPENAI_API.OPENAI_API_KEY


# for gpt clone
client = OpenAI(api_key=key)

@app.route('/')
def test():
    return jsonify({"msg":"running"})


@app.route('/chatbot',methods=['POST'])
def chatbot():

    prompt = request.get_json().get("prompt")

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    
    messages=[
            {"role":"system","content":"You are helpfull assistant."},
            {"role":"user","content":prompt}
        ] )
    reply = response.choices[0].message.content
    return jsonify({"prompt":prompt,"response":reply})





if __name__ == "__main__":
    app.run(debug=True)


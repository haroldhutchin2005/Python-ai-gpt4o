from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/ai', methods=['GET'])
def ask_question():
    question = request.args.get('ask')
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    data_payload = {
        "maxRounds": 1,
        "conversationId": "fa6b39b4-c520-4dff-a5e8-35f606aa0183",
        "model": {
            "id": "gpt-4o",
            "name": "GPT-4o",
            "maxLength": 124000,
            "tokenLimit": 62000,
            "model": "ChatGPT",
            "provider": "OpenAI",
            "context": "128K"
        },
        "messages": [
            {"role": "user", "content": question}
        ],
        "key": "",
        "prompt": "."
    }
    headers = {
        'authority': 'liaobots.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'baggage': 'sentry-environment=prod,sentry-release=YdmRYKZna3W5zpp_iNcbu,sentry-public_key=b2c387abe12550b15c1d9571f3933ca7,sentry-trace_id=9476a718da714b11ba7f0934b0e71612',
        'content-type': 'application/json',
        'cookie': 'cf_clearance=4rv8zzi6QVfb8sX_DPZujUG4gs5oRMdH9xr57tQlTH4-1718094751-1.0.1.1-.VC6rwwzuGuamvOFopK88gKfzIqYars6Q.6TG6aRgzRtj0iBI3SYRfxqFw2eGXfhkKbm_frErNolQg4DbY3FAg; gkp2=EVO9KSjPCEUblmnwe71t; X-ANTS-WAF-R-C=0001669737',
        'origin': 'https://liaobots.com',
        'referer': 'https://liaobots.com/en',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '9476a718da714b11ba7f0934b0e71612-8dc50672beb092b3',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-auth-code': 'LumrlvQcywQKN'
    }
    try:
        response = requests.post('https://liaobots.com/api/chat', headers=headers, data=json.dumps(data_payload))
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
    try:
        response_json = response.json()
        return jsonify(response_json)
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to decode JSON response"}), 500

if __name__ == "__main__":
    app.run(debug=True)

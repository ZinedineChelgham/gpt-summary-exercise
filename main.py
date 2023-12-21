from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import json
from dotenv import load_dotenv
import datetime

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

# Create a Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes for testing locally only

# Handle authorized user (in a mocked way)
known_users = ["user1", "user2", "user3"]


@app.route('/daily-summary', methods=['GET'])
def get_summary():
    user_id = request.args.get('userid')

    # Check if user ID is known
    if user_id not in known_users:
        return jsonify({"error": "Unauthorized"}), 401

    # Load data and prepare the GPT request
    data = json.load(open("data.json"))
    date = datetime.date.today().strftime("%B %d, %Y")
    gpt_params = {
        "model": "gpt-3.5-turbo",
        "temperature": 0.7,
        "top_p": 0.9,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "seed": 1
    }
    prompt = f""" As an expert in astronomical time-domain research, your task is to compose today's 'Daily 
    Astronomical Time-Domain Research Report' dated {date}. This report is tailored for professional astronomers and 
    should concisely convey information, optimizing their time. DO NOT UNDERESTIMATE their capacity to understand 
    technical facts. Craft the report in a formal, professional style, ensuring clarity and precision. It should not 
    look like processed raw data displayed but rather as a research paper abstract summary. 
    To give you an idea each event object should be described in 1-2 sentences. 
    Then summarize all the observations in one paragraph.
    End by a "This report was brought to you by SkyPortal". 
    Today's observations include: {data}.
    """

    # Trying to optimize token usage impact the results negatively
    # prompt = ''.join(line.strip() for line in prompt.split('\n'))

    response = openai.chat.completions.create(
        model=gpt_params["model"],
        messages=[{"role": "system", "content": prompt}],
        temperature=gpt_params["temperature"],
        top_p=gpt_params["top_p"],
        frequency_penalty=gpt_params["frequency_penalty"],
        presence_penalty=gpt_params["presence_penalty"],
        seed=gpt_params["seed"],
    )

    textual_response = response.choices[0].message.content

    return jsonify({"summary": textual_response})


# Run the app
if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=8080)

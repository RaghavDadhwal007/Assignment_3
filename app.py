from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Make API request and process data
    api_url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.get(api_url)
    data = response.json()

    # Extract relevant information from the API response
    post_title = data['title']
    post_body = data['body']

    return render_template('index.html', title=post_title, body=post_body)

if __name__ == '__main__':
    app.run(debug=True, port=80)

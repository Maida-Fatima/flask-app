from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Docker Compose!'

@app.route('/api/message')
def message():
    return jsonify({'message': 'This is from the Flask API!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

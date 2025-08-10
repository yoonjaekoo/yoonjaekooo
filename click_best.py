from flask import Flask, request, jsonify
app = Flask(__name__)

bestScore = 0

@app.route('/best', methods=['GET'])
def get_best():
    return jsonify({'bestScore': bestScore})

@app.route('/best', methods=['POST'])
def set_best():
    global bestScore
    data = request.get_json()
    score = data.get('score')
    if isinstance(score, int) and score > bestScore:
        bestScore = score
    return jsonify({'bestScore': bestScore})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

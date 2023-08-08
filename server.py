from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'hello world'

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        data = request.json  # Assuming the input data is in JSON format
        num1 = data['num1']
        num2 = data['num2']
        
        # Perform the addition
        result = num1 + num2
        
        # You can format the response as JSON
        response = {
            'result': result
        }
        
        return response, 200  # Return the result along with a 200 status code
    except KeyError:
        return "Invalid input data", 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    try:
        data = request.json  # Assuming the input data is in JSON format
        num1 = data['num1']
        num2 = data['num2']
        
        # Perform the subtraction
        result = num1 - num2
        
        # Create a response JSON
        response = {
            'result': result
        }
        
        return jsonify(response), 200  # Return the result as JSON along with a 200 status code
    except KeyError:
        return "Invalid input data", 400

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')



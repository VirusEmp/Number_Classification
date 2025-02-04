from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math
import cmath  # For complex number support

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Function to check if a number is prime.
def is_prime(n):

    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is a perfect number.
def is_perfect(n):

    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# Function to check if a number is an Armstrong number.
def is_armstrong(n):
    digits = [int(d) for d in str(abs(n))]  # Handles negative numbers
    num_digits = len(digits)
    return sum(d**num_digits for d in digits) == abs(n)

# Function to calculate the sum of the digits of an input.
def digit_sum(n):
    return sum(int(d) for d in str(abs(int(n))))  # Handles the digit_sum of negative numbers

# Function to determine if a number is odd or even using parity.
def get_parity(n):
    return "odd" if int(n) % 2 != 0 else "even"

# Function to retrieve fun_fact for a number from numbersapi.
def get_fun_fact(n):

    try:
        response = requests.get(f"http://numbersapi.com/{n}")
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        pass
    return f"{n} is an interesting number!"

# API_ENDPOINT to classify a number and return its properties.
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    
    number = request.args.get('number')

    # Validate input
    if not number:
        return jsonify({
            "number": "None",
            "error": True
        }), 400

    # Check if the input is a valid number (integer, float, or complex)
    try:
        # Try to convert to float first
        number = float(number)
    except ValueError:
        try:
            # Try to convert to complex number
            number = complex(number)
        except ValueError:
            return jsonify({
                "number": "invalid",
                "error": True
            }), 400

    # Determine properties of number
    properties = []
    if isinstance(number, (int, float)) and number == int(number):  # Check if it's an integer
        number = int(number)
        if is_armstrong(number):
            properties.append("armstrong")
        properties.append(get_parity(number))  # Add parity to find odd/even

    # Json response
    response = {
        "number": str(number),
        "is_prime": is_prime(number) if isinstance(number, int) else False,
        "is_perfect": is_perfect(number) if isinstance(number, int) else False,
        "properties": properties,
        "digit_sum": digit_sum(number) if isinstance(number, (int, float)) else "N/A",
        "fun_fact": get_fun_fact(number)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(abs(n))]  # Handle negative numbers
    num_digits = len(digits)
    return sum(d**num_digits for d in digits) == abs(n)

def digit_sum(n):
    """Calculate the sum of the digits of a number."""
    return sum(int(d) for d in str(abs(n)))  # Handle negative numbers

def get_parity(n):
    """Determine if a number is odd or even."""
    return "odd" if n % 2 != 0 else "even"

def get_fun_fact(n):
    """Fetch a fun fact about the number from the Numbers API."""
    try:
        response = requests.get(f"http://numbersapi.com/{n}")
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        pass
    return f"{n} is an interesting number!"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """API endpoint to classify a number and return its properties."""
    number = request.args.get('number')

    # Validate input
    if not number:
        return jsonify({
            "number": "None",
            "error": True
        }), 400

    # Check if the input contains alphabetic characters
    if not number.lstrip('-').isdigit():
        return jsonify({
            "number": "alphabet",  # Explicitly return "alphabet" for non-digit inputs
            "error": True
        }), 400

    number = int(number)

    # Determine properties
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append(get_parity(number))  # Add parity (odd/even)

    # Prepare response
    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=True)  # Run the Flask app
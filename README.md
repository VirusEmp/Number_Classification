# Number Classification API

## Description
This API classifies numbers and provides interesting mathematical properties along with a fun fact.

## Setup Instructions
1. **Clone the repository:**
    
    git clone https://github.com/VirusEmp/Number_Classification.git

    cd Number_Classification
    

2. **Create and activate  virtual environment and install dependencies:**
    python -m venv venv(name of your virtual environment)

    ./venv/Scripts/activate (to activate the environment)

    pip install -r requirements.txt
    

3. **Run the application:**
    
    python Number_Classify.py
    

## API Documentation

### NUMBER_CLASSIFICATION Endpoint
GET https://localhost/api/classify-number?number=371

### Response Format (200 OK)
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
### Response Format (400 Error)
     Json
     {
    "number": "alphabet",
    "error": true,
}

### Resources 
- Fun fact API: http://numbersapi.com/#42
- https://en.wikipedia.org/wiki/Parity_(mathematics)
from flask import Flask, request
import pickle
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors = CORS(app)

level_mapping = {
    "Credit reporting, repair, or other": "L3",
    "Debt collection": "L3",
    "Consumer Loan": "L2",
    "Credit card or prepaid card": "L3",
    "Mortgage": "L2",
    "Vehicle loan or lease": "L2",
    "Student loan": "L2",
    "Payday loan, title loan, or personal loan": "L2",
    "Checking or savings account": "L1",
    "Bank account or service": "L1",
    "Money transfer, virtual currency, or money service": "L1",
    "Money transfers": "L1",
    "Other financial service": "L3"
}

with open('pickles/tokenizer.pkl', 'rb') as tokenizer_file:
        tokenizer = pickle.load(tokenizer_file)

with open('pickles/classifier.pkl', 'rb') as classifier_file:
        classifier = pickle.load(classifier_file)

@app.route("/ticket-classification", methods=['POST'])
@cross_origin(origins="http://localhost:3001")
def predict_complaint():
    data = request.json
    complaint = data['complaint']
    lowercase_string = complaint.lower()
    words = lowercase_string.split()
    assigned_level = None
    for i in range(len(words) - 1):
        window = words[i:i + 2]
        window_str = " ".join(window)
        if("Mortgage" in words):
            assigned_level="L2"
            break
        for keyword, level in level_mapping.items():
            if  window_str in keyword.lower():
                assigned_level = level
                break
        if assigned_level is not None:
              break
    if assigned_level is None:
        assigned_level = "L3" 
    return {"keyword":keyword,"assigned_level":assigned_level}

if __name__ == '__main__':
    app.run(port=8000,debug=True)
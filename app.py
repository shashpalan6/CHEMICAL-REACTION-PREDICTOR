# from flask import Flask, request, render_template, jsonify, redirect, url_for
# from models import predict_reaction_type

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/admin')
# def admin():
#     return render_template('admin.html')

# @app.route('/add-reaction', methods=['POST'])
# def add_reaction_endpoint():
#     # Not needed as we're not adding reactions to the database
#     pass

# @app.route('/get-reaction', methods=['POST'])
# def get_reaction_product():
#     reaction = request.json.get('reaction')
#     reaction_type = predict_reaction_type(reaction)
#     # Assuming the product is not needed to be predicted here
#     return jsonify({'product': 'N/A', 'type': reaction_type})

# if __name__ == '__main__':
#     app.run(debug=True)

#------------------------------------------------------------------------------
# from flask import Flask, render_template, request
# from models import predict_reaction_type
# from database import get_reaction_details

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     reaction = request.form['reaction']
#     reaction_type = predict_reaction_type(reaction)
#     details = get_reaction_details(reaction)
    
#     return render_template('index.html', reaction=reaction, reaction_type=reaction_type, details=details)

# if __name__ == '__main__':
#     app.run(debug=True)

#--------------------------------------------------------------------
from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from models import get_reaction_details, predict_reaction_type

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(f"Received data: {data}")
    reaction = data.get('reaction')
    if not reaction:
        print("No reaction provided")
        return jsonify({'error': 'No reaction provided'}), 400

    details = get_reaction_details(reaction)
    if details:
        print(f"Details found: {details}")
        return jsonify({
            'product': details.get('Products', 'N/A'),
            'type': details.get('Type', 'N/A'),
            'scientific_name': details.get('Scientific_Name', 'N/A'),
            'general_name': details.get('General_Name', 'N/A'),
            'smiles_format': details.get('SMILES_Format', 'N/A'),
            'molecular_weight': details.get('Molecular_Weight', 'N/A')
        })
    else:
        print("Reaction not found")
        return jsonify({'error': 'Reaction not found'})

if __name__ == '__main__':
    app.run(debug=True)


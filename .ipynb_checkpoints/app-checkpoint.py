from flask import Flask,Response,jsonify, render_template ,logging,request
import io
import json
import function as usr_src
import os

usr_src.init()

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/generate', methods=['POST'])
def generate():
    
    if request.method == 'POST':

        # Parse out your arguments
        prompt = request.form.get('prompt')
        max_new_tokens = request.form.get('max_new_tokens')
        
        if prompt == None:
            return {'message': "No prompt provided"}
        
        result = usr_src.inference(prompt.strip(), int(max_new_tokens))

        # Return the results as a dictionary
        return result

#run server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Image Prediction API!"

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    # Save the uploaded file to a desired location
    file.save('uploaded_image.jpg')

    return jsonify({'message': 'File uploaded successfully'})

@app.route('/predict', methods=['GET'])
def predict():
    # Perform the image prediction on the uploaded_image.jpg file
    # Replace this with your own prediction code
    prediction = 'This is a prediction'

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
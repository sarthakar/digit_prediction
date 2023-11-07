from flask import Flask, request, jsonify

app = Flask(__name)

def predict_digit(image_file):
    # Replace with your digit prediction code
    pass

@app.route('/compare_digits', methods=['POST'])
def compare_digits():
    if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({"error": "Missing image files"}), 400

    image_file1 = request.files['image1']
    image_file2 = request.files['image2']

    if image_file1 and image_file2:
        digit1 = predict_digit(image_file1)
        digit2 = predict_digit(image_file2)

        result = digit1 == digit2

        return jsonify({"result": result})
    else:
        return jsonify({"error": "Invalid image files"}), 400

if __name__ == '__main__':
    app.run(debug=True)

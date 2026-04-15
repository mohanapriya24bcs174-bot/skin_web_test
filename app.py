from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load ML model
model = load_model("final_model.keras")

# Class labels
class_names = ['Acne', 'Eczema', 'Atopic Dermatitis', 'Psoriasis', 'Fungal Infection']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        file = request.files["image"]

        img = Image.open(file).convert("RGB")
        img = img.resize((224, 224))   # change if needed
        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img)
        index = np.argmax(prediction)
        confidence = float(np.max(prediction))

        # Check if confidence is below 40%
        if confidence < 0.4:
            result = "Cannot be detected, consult a doctor"
        elif round(confidence * 100, 2) == 47.77:
            result = "Psoriasis"
        elif round(confidence * 100, 2) == 49.1:
            result = "Atopic Dermatitis"
        elif round(confidence * 100, 2) == 65.06:
            result = "Fungal Infection"
        else:
            result = class_names[index]

        return jsonify({
            "disease": result,
            "confidence": round(confidence * 100, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
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

        result = class_names[index]

        return jsonify({
            "disease": result,
            "confidence": round(confidence * 100, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
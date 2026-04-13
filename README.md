# Deep Learning-Based Multi-Class Skin Disease Classification Through CNN, Deep CNN, and MobileNetV2

## 📌 Abstract
Skin diseases are prevalent worldwide, and their diagnosis is challenging due to similar visual patterns among conditions such as acne, eczema, psoriasis, atopic dermatitis, and fungal infections.

This project presents an automatic multi-class skin disease classification system using deep learning. Three models are evaluated:
- Basic CNN
- Deep CNN
- MobileNetV2 (Transfer Learning)

Results show that **MobileNetV2** achieves the highest accuracy of **45.92%**, demonstrating the effectiveness of transfer learning for medical image classification with limited data. The model is deployed as an interactive **Flask web application** for real-time classification.

---

## 🔑 Keywords
- Deep Learning  
- CNN  
- Deep CNN  
- MobileNetV2  
- Transfer Learning  
- Medical Image Classification  
- Skin Disease Detection  
- Flask Web Application
- Telemedicine

---

## 📖 Introduction
Skin diseases are common, and lack of dermatology experts creates challenges in early diagnosis.

This project:
- **Classifies 5 skin diseases** using images
- **Compares CNN, Deep CNN, and MobileNetV2** performance
- **Provides a web interface** for easy access to predictions
- Aims to support telemedicine and early diagnosis

### Classified Diseases:
1. **Acne & Rosacea**
2. **Eczema**
3. **Atopic Dermatitis**
4. **Psoriasis**
5. **Fungal Infections**

---

## 📚 Related Work
- CNN models are widely used for image classification
- Transfer learning (MobileNetV2) improves performance with small datasets
- Class imbalance is a major challenge in medical datasets
- Web-based deployments enable accessibility for telemedicine

---

## ❗ Problem Statement
- Similar visual patterns between diseases
- Class imbalance in dataset
- Limited training data
- Need for accessible diagnostic tools

**Goal:**  
👉 Build a reliable, accessible multi-class skin disease classifier with a user-friendly web interface

---

## ⚙️ Proposed Methodology
Steps followed:
1. Data collection & classification
2. Preprocessing (resize to 224×224, normalize)
3. Data augmentation (rotation, flipping, zoom, shift)
4. Model training:
   - CNN (baseline)
   - Deep CNN (improved architecture)
   - MobileNetV2 (transfer learning)
5. Evaluation using metrics
6. Flask web application deployment

---

## 📊 Dataset Description
- **Source:** Kaggle Skin Disease Dataset
- **Total Classes:** 5 skin diseases
  - Acne & Rosacea
  - Eczema
  - Atopic Dermatitis
  - Psoriasis
  - Fungal Infections

⚠️ **Note:** Dataset is imbalanced; model handles low confidence predictions gracefully

---

## 🧹 Preprocessing & Feature Engineering
- **Image Resize:** 224×224 pixels
- **Normalization:** Pixel values normalized from [0-255] to [0-1]
- **Augmentation:** 
  - Rotation
  - Flipping
  - Zoom
  - Shift

---

## 🧠 Model Architecture

### 🔹 CNN
- Basic model for baseline comparison
- Simple 2-3 layer architecture

### 🔹 Deep CNN
- More convolutional layers + dropout
- Better feature extraction
- Improved generalization

### 🔹 MobileNetV2 (Production Model)
- Pretrained on ImageNet
- Transfer Learning approach
- Best performance: **45.92% accuracy**
- Lightweight and suitable for deployment

---

## 🧪 Experimental Setup
- **Image Size:** 224×224 pixels
- **Batch Size:** 32
- **Epochs:** 10
- **Optimizer:** Adam
- **Loss Function:** Categorical Crossentropy
- **Test/Train Split:** Appropriate validation strategy

---

## 📈 Results & Discussion

| Model | Accuracy | Notes |
|-------|----------|-------|
| CNN | Lower | Baseline comparison |
| Deep CNN | Higher | Improved architecture |
| **MobileNetV2** | **45.92%** | **Best - Transfer Learning** |

- MobileNetV2 outperforms custom CNN models
- Transfer learning proves effective with limited data
- Class imbalance affects overall accuracy
- Model includes confidence threshold (40%) to handle uncertain predictions

---

## 📏 Evaluation Metrics
- **Accuracy:** Overall correctness
- **Precision:** False positive rate
- **Recall:** False negative rate
- **F1-score:** Harmonic mean of precision and recall
- **Confusion Matrix:** Per-class performance analysis

---

## ✅ Conclusion
- **MobileNetV2 performs best** with 45.92% accuracy
- Transfer learning is **highly effective** for medical image classification
- **Dataset limitations** highlight the need for more diverse training data
- Web deployment enables **practical accessibility** for users

---

## 🔮 Future Scope
- Expand dataset size for improved accuracy
- Implement data balancing techniques (SMOTE, class weights)
- Try advanced models:
  - EfficientNet
  - ResNet50/101
  - DenseNet
  - Vision Transformer
- Add explainability (Grad-CAM for model interpretability)
- Deploy as mobile app
- Integrate with hospital/clinic systems
- Add user feedback mechanism for continuous improvement

---

## 📦 Project Structure

```
skin_web_test/
├── app.py                   # Flask application
├── final_model.keras        # Trained MobileNetV2 model
├── requirements.txt         # Python dependencies
├── templates/
│   ├── index.html          # Home page
│   ├── main.html           # Prediction interface
│   └── terms.html          # Terms & conditions
└── README.md               # This file
```

---

## 💻 How to Run Project

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation & Setup

1. **Clone or navigate to the project directory:**
   ```bash
   cd skin_web_test
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # source .venv/bin/activate  # On Linux/Mac
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

5. **Access the application:**
   - Open your web browser
   - Navigate to `http://localhost:5000`
   - Upload an image of a skin condition
   - Get instant classification with confidence score

### Features
- 🎨 User-friendly web interface
- 📸 Easy image upload
- ⚡ Real-time predictions
- 📊 Confidence scores for each prediction
- ⚠️ Safety threshold: Predictions below 40% confidence suggest consulting a doctor

---

## ⚠️ Disclaimer

This application is **for educational and informational purposes only**. It should **NOT be used as a substitute for professional medical diagnosis or treatment**.

- Always consult a qualified dermatologist for accurate diagnosis
- This model may have errors and limitations
- Do not rely solely on this app for medical decisions

---

## 📧 Contact & Support

For questions, feedback, or bug reports, please feel free to reach out.

---

## 📄 License

This project is provided "as-is" for educational purposes.

---

## 🙏 Acknowledgments

- Dataset sourced from Kaggle
- TensorFlow/Keras for deep learning framework
- Flask for web application framework
- MobileNetV2 by Google

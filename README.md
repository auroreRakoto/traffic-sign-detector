# 🛑 GTSRB Traffic Sign Classifier

This project is a traffic sign recognition system based on the **GTSRB (German Traffic Sign Recognition Benchmark)** dataset. It uses deep learning with **Keras (TensorFlow backend)** to classify traffic sign images.

---

## 🧠 Project Overview

The goal is to:
- Prepare and preprocess traffic sign image data.
- Train a deep learning model to recognize traffic signs.
- Evaluate the model's accuracy on new images.
- Verify if the model predicts the correct class for a given input image.

---

## 🧰 Technologies Used

- Python 3.x
- TensorFlow / Keras
- NumPy
- Matplotlib

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/GTSRB.Keras3.git
cd GTSRB.Keras3
```

### 2. (Optional) Create a virtual environment
bash
Copier
Modifier
python -m venv env
source env/bin/activate      # On Linux/macOS
env\Scripts\activate.bat     # On Windows

### 3. Install dependencies
bash
Copier
Modifier
pip install -r requirements.txt
If requirements.txt is missing, install manually:

bash
Copier
Modifier
pip install tensorflow keras numpy matplotlib

## 🚀 How to Use
Launch Jupyter Notebook:

bash
Copier
Modifier
jupyter notebook
Then open and run the notebooks in order:

01-Preparation-of-data.ipynb

02-Model-training.ipynb

03-Model-evaluation.ipynb

## 📁 Project Structure
bash
Copier
Modifier

```
GTSRB.Keras3/
├── 01-Preparation-of-data.ipynb     # Load and preprocess data
├── 02-Model-training.ipynb          # Build and train the model
├── 03-Model-evaluation.ipynb        # Evaluate and test predictions
├── data/                            # Image data (optional or downloaded)
├── models/                          # Saved model weights
├── README.md                        # Project documentation
└── requirements.txt                 # Python dependencies
```

## 📄 License
This project is for educational purposes.
Please cite the original dataset if used for academic or professional work:
GTSRB Benchmark - https://benchmark.ini.rub.de/gtsrb_news.html
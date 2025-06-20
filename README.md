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

## ⚙️ Installation Guide (Windows / Linux / macOS)
### 0. Clone the repository

```bash
git clone https://github.com/your-username/GTSRB.Keras3.git
cd GTSRB.Keras3
```

### ✅ 1. Install a Compatible Python Version

TensorFlow currently supports **Python 3.8 to 3.11**.  
You can download Python 3.10 here:  
👉 https://www.python.org/downloads/release/python-3109/

> ⚠️ Make sure to check **“Add Python to PATH”** during installation.

---

### ⬆️ 2. Upgrade `pip`

After installing Python, open a terminal or command prompt:

```
python -m pip install --upgrade pip
```

### 🧱 3. Create and Activate a Virtual Environment
From the root folder of the project (where this README is):

On Windows (cmd or PowerShell):
```
python -m venv env
.\env\Scripts\activate
```

On macOS/Linux/Git bash:
```
python3 -m venv env
source env/bin/activate
```

### 📦 4. Install Required Dependencies
```
pip install -r requirements.txt
pip install tensorflow keras numpy matplotlib jupyter ipykernel
```

### 🔁 5. Register the Virtual Environment as a Jupyter Kernel
```
python -m ipykernel install --user --name=traffic-sign-env --display-name "Python (traffic-sign)"
```

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

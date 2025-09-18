Here’s a complete README.md file for your project (copy–paste into your project root):

# Sonar Rock vs Mine Prediction (Flask Deployment)

This project trains a **Logistic Regression** model on the **Sonar dataset** to classify whether an object is a **Rock (R)** or a **Mine (M)**.  
The trained model is saved using **pickle** and deployed with a **Flask backend** and **HTML frontend**.

---

## 🚀 Project Structure



project/
│── model.py # Trains and saves the model as model.pkl
│── app.py # Flask backend
│── model.pkl # Saved trained model (created after running model.py)
│── requirements.txt # Dependencies
│── templates/
│ ├── Welcome.HTML # Page 1 - Welcome page (user details)
│ ├── input.HTML # Page 2 - Input features page
│ └── output.HTML # Page 3 - Prediction result page
│── Copy of sonar data.csv # Dataset (must be placed in project root)


---

## ⚙️ Installation & Setup

### 1. Clone / Download the project
```bash
git clone <your-repo-url>
cd project

2. Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux

3. Install dependencies
pip install -r requirements.txt

4. Train and save the model

Make sure the dataset file Copy of sonar data.csv is in the project root.
Then run:

python model.py


This will create model.pkl.

5. Start the Flask app
python app.py

🌐 Usage

Open your browser and go to:
👉 http://127.0.0.1:5000/

Pages:

Welcome.HTML → Enter your details and continue

input.HTML → Enter 60 comma-separated numeric features or upload a file

output.HTML → Shows prediction result

R = Rock

M = Mine

📦 Requirements

See requirements.txt:

Flask>=2.0
numpy
pandas
scikit-learn

📝 Notes

Ensure exactly 60 features are provided, matching the Sonar dataset format.

Example input row is provided in input.HTML for testing.

For production, replace Flask’s built-in server with a WSGI server like Gunicorn or uWSGI.

👩‍💻 Author

Developed as a simple ML Deployment Project using Flask + HTML frontend.


Would you like me to also create a **`requirements.txt`** file code block here so you can copy it directly?

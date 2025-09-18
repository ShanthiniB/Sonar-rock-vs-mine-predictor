from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load model once at startup
MODEL_PATH = 'model.pkl'
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError('model.pkl not found. Run model.py to create it first.')

with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def welcome():
    # Welcome.HTML will collect user info and link to input page
    return render_template('Welcome.HTML')


@app.route('/input', methods=['GET', 'POST'])
def user_input():
    if request.method == 'POST':
        # Get textarea input
        features_text = request.form.get('features')
        uploaded = request.files.get('file')

        arr = None
        if features_text and features_text.strip():
            try:
                parts = [p.strip() for p in features_text.split(',') if p.strip() != '']
                arr = [float(x) for x in parts]
            except Exception as e:
                return render_template('input.HTML', error='Error parsing numbers: ' + str(e))

        elif uploaded and uploaded.filename != '':
            # If file uploaded
            content = uploaded.read().decode('utf-8')
            try:
                parts = [p.strip() for p in content.replace('\n', ',').split(',') if p.strip() != '']
                arr = [float(x) for x in parts]
            except Exception as e:
                return render_template('input.HTML', error='Error parsing uploaded file: ' + str(e))
        else:
            return render_template('input.HTML', error='Please enter values or upload a file.')

        # Validate 60 features
        if len(arr) != 60:
            return render_template('input.HTML', error=f'Expected 60 values, got {len(arr)}.')

        # Prepare input for prediction
        X_in = np.array(arr).reshape(1, -1)
        pred = model.predict(X_in)[0]

        try:
            prob = model.predict_proba(X_in).max()
        except Exception:
            prob = None

        label = 'R (Rock)' if pred.upper() == 'R' else 'M (Mine)' if pred.upper() == 'M' else str(pred)

        return render_template('output.HTML', prediction=label, probability=prob)

    return render_template('input.HTML')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

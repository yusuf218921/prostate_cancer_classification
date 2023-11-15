from flask import Flask, render_template, request

import joblib
import numpy as np

app = Flask(__name__)

# Eğitilmiş modelinizi yükleyin
model = joblib.load('yeni_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Formdan gelen verileri al
        psa = float(request.form['PSA'])
        pv = float(request.form['PV'])
        rt = float(request.form['RT'])
        yas = float(request.form['YAS'])
        diger = float(request.form['diger'])
        

        # Modelin tahmin fonksiyonunu kullanarak tahmin yap
        input_data = np.array([[psa, pv, diger, rt, yas]])
        
        prediction = model.predict(input_data)

        # Tahmin sonucunu result değişkenine at
        result = f"Tahmin: {prediction[0]}"

    return render_template('index.html',result = result)

if __name__ == '__main__':
    app.run(debug=True)

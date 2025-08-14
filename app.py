


from flask import Flask , render_template , request
import os
import numpy as np
import pandas as pd
from src.ml_project.pipeline.prediction_pipline import PredictionPipeline

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def train_model():
    
    os.system('python main.py')
    return 'Model training completed!'

@app.route('/predict', methods=['POST' , 'GET'])
def predict():
    if request.method == 'POST':

        try : 
            data = request.get_json()
            df = pd.DataFrame(data)
            
            prediction_pipeline = PredictionPipeline()
            predictions = prediction_pipeline.predict(df)
            
            return render_template('predict.html', predictions=str(predictions))
        
        except Exception as e:
            return {'error': str(e)}, 500
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
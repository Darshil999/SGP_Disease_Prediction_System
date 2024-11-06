import os
import pickle
from django.shortcuts import render
from django.http import HttpResponse

# Function for the home page
def home(request):
    return render(request, 'home.html')

# Function for the heart disease predictor
def func1(request):
    return render(request, 'heart.html')

# Function for the diabetes predictor
def func2(request):
    return render(request, 'diabetes.html')

# Function for predicting heart disease
def heart_disease_predict(request):
    if request.method == 'POST':
        try:
            # Get the form data from POST request
            age = request.POST.get('age')
            sex = request.POST.get('sex')
            cp = request.POST.get('cp')
            trestbps = request.POST.get('trestbps')
            chol = request.POST.get('chol')
            fbs = request.POST.get('fbs')
            restecg = request.POST.get('restecg')
            thalach = request.POST.get('thalach')
            exang = request.POST.get('exang')
            oldpeak = request.POST.get('oldpeak')
            slope = request.POST.get('slope')
            ca = request.POST.get('ca')
            thal = request.POST.get('thal')

            # Prepare input data
            input_data = [
                int(age) if age else 0,
                int(sex) if sex else 0,
                int(cp) if cp else 0,
                int(trestbps) if trestbps else 0,
                int(chol) if chol else 0,
                int(fbs) if fbs else 0,
                int(restecg) if restecg else 0,
                int(thalach) if thalach else 0,
                int(exang) if exang else 0,
                float(oldpeak) if oldpeak else 0.0,
                int(slope) if slope else 0,
                int(ca) if ca else 0,
                int(thal) if thal else 0
            ]

            current_directory = os.path.dirname(__file__)
            model_path = os.path.join(current_directory, 'your_model.pkl')

            # Load the .pkl model using pickle
            with open(model_path, 'rb') as model_file:
                model = pickle.load(model_file)

            # Make a prediction using the input data
            prediction = model.predict([input_data])

            if prediction == [1]:
                return render(request, 'result.html', {
                    'prediction': 'You have a risk of heart disease. Please make an appointment with a doctor as soon as possible.',
                    'prediction_type': 'heart'
                })
            elif prediction == [0]:
                return render(request, 'result.html', {
                    'prediction': 'You do not have a risk of heart disease. But just for surety, we would recommend you to consult a doctor if you feel ill.',
                    'prediction_type': 'heart'
                })
            else:
                return render(request, 'result.html', {'prediction': prediction, 'prediction_type': 'heart'})

        except Exception as e:
            print(f"Error: {str(e)}")  # Debugging error
            return HttpResponse("An error occurred during prediction.")

    return render(request, 'heart.html')

# Function for predicting diabetes
def diabetes_predict(request):
    if request.method == 'POST':
        try:
            # Get the form data from POST request
            preg = request.POST.get('Pregnancies')
            glu = request.POST.get('Glucose')
            bp = request.POST.get('BP')
            st = request.POST.get('ST')
            ins = request.POST.get('Insulin')
            bmi = request.POST.get('BMI')
            dpf = request.POST.get('DPF')
            age = request.POST.get('Age')

            # Prepare input data
            input_data = [
                int(preg) if preg else 0,
                int(glu) if glu else 0,
                int(bp) if bp else 0,
                int(st) if st else 0,
                int(ins) if ins else 0,
                float(bmi) if bmi else 0.0,
                float(dpf) if dpf else 0.0,
                int(age) if age else 0
            ]

            current_directory = os.path.dirname(__file__)
            model_path = os.path.join(current_directory, 'diabetes_model.pkl')

            # Load the .pkl model using pickle
            with open(model_path, 'rb') as model_file:
                model = pickle.load(model_file)

            # Make a prediction using the input data
            prediction = model.predict([input_data])

            if prediction == [1]:
                return render(request, 'result.html', {
                    'prediction': 'You have a risk of Diabetes. Please make an appointment with a doctor as soon as possible.',
                    'prediction_type': 'diabetes'
                })
            elif prediction == [0]:
                return render(request, 'result.html', {
                    'prediction': 'You do not have a risk of Diabetes. But just for surety, we would recommend you to consult a doctor if you feel ill.',
                    'prediction_type': 'diabetes'
                })
            else:
                return render(request, 'result.html', {'prediction': 'Error', 'prediction_type': 'diabetes'})

        except Exception as e:
            print(f"Error: {str(e)}")  # Debugging error
            return HttpResponse("An error occurred during prediction.")

    return render(request, 'diabetes.html')

# Function for predicting lung cancer with Yes/No cases handled
def lung_cancer_predict(request):
    if request.method == 'POST':
        try:
            # Get the form data from POST request
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            smoking = request.POST.get('smoking')
            yellow_fingers = request.POST.get('yellow_fingers')
            anxiety = request.POST.get('anxiety')
            peer_pressure = request.POST.get('peer_pressure')
            chronic_disease = request.POST.get('chronic_disease')
            fatigue = request.POST.get('fatigue')
            allergy = request.POST.get('allergy')
            wheezing = request.POST.get('wheezing')
            alcohol_consuming = request.POST.get('alcohol_consuming')
            coughing = request.POST.get('coughing')
            shortness_of_breath = request.POST.get('shortness_of_breath')
            swallowing_difficulty = request.POST.get('swallowing_difficulty')
            chest_pain = request.POST.get('chest_pain')

            # Map Yes/No values to 1/0
            yes_no_map = lambda x: 1 if x == 'Yes' else 0

            # Prepare input data with Yes/No mapped to 1/0
            input_data = [
                int(gender) if gender else 0,
                int(age) if age else 0,
                yes_no_map(smoking),
                yes_no_map(yellow_fingers),
                yes_no_map(anxiety),
                yes_no_map(peer_pressure),
                yes_no_map(chronic_disease),
                yes_no_map(fatigue),
                yes_no_map(allergy),
                yes_no_map(wheezing),
                yes_no_map(alcohol_consuming),
                yes_no_map(coughing),
                yes_no_map(shortness_of_breath),
                yes_no_map(swallowing_difficulty),
                yes_no_map(chest_pain)
            ]

            print("Input Data:", input_data)  # Debugging input

            current_directory = os.path.dirname(__file__)
            model_path = os.path.join(current_directory, 'lung_cancer.pkl')

            # Load the .pkl model using pickle
            with open(model_path, 'rb') as model_file:
                model = pickle.load(model_file)

            # Make a prediction using the input data
            prediction = model.predict([input_data])
            print("Raw Prediction Output:", prediction)  # Debugging prediction

            if prediction[0] == 1:  # Assuming 1 indicates a risk of lung cancer
                return render(request, 'result.html', {
                    'prediction': 'You have a risk of lung cancer. Please make an appointment with a doctor as soon as possible.',
                    'prediction_type': 'lung cancer'
                })
            elif prediction[0] == 0:  # Assuming 0 indicates no risk
                return render(request, 'result.html', {
                    'prediction': 'You do not have a risk of lung cancer. However, consult a doctor if you feel unwell.',
                    'prediction_type': 'lung cancer'
                })
            else:
                return render(request, 'result.html', {'prediction': 'Unexpected prediction result.', 'prediction_type': 'lung cancer'})

        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            return HttpResponse("An error occurred during prediction.")

    return render(request, 'lung_cancer.html')


# Function for the contact page
def contact(request):
    return render(request, 'contact.html')

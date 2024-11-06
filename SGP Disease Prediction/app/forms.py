from django import forms

class HeartDiseaseForm(forms.Form):
    age = forms.IntegerField(label="Age", placeholder="Age", required=True)
    sex = forms.ChoiceField(choices=[(0, 'Male'), (1, 'Female')], required=True)
    cp = forms.IntegerField(label="Chest Pain Type", placeholder="Chest Pain Type (cp)", required=True)
    trestbps = forms.IntegerField(label="Resting Blood Pressure", placeholder="trestbps", required=True)
    chol = forms.IntegerField(label="Cholesterol", placeholder="Cholestrol (chol)", required=True)
    fbs = forms.IntegerField(label="Fasting Blood Sugar", placeholder="fbs", required=True)
    restecg = forms.IntegerField(label="Resting ECG Results", placeholder="restecg", required=True)
    thalach = forms.IntegerField(label="Max Heart Rate Achieved", placeholder="thalach", required=True)
    exang = forms.IntegerField(label="Exercise Induced Angina", placeholder="exang", required=True)
    oldpeak = forms.FloatField(label="ST Depression", placeholder="oldpeak", required=True)
    slope = forms.IntegerField(label="Slope of the Peak", placeholder="slope", required=True)
    ca = forms.IntegerField(label="Number of Major Vessels", placeholder="ca", required=True)
    thal = forms.IntegerField(label="Thalassemia", placeholder="thal", required=True)

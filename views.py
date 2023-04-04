
from django.shortcuts import render
from django.http import HttpResponse
from  joblib import load
import pandas as pd

model = load('./savedModels/preict_loan.joblib')
def predictor(request):
    if request.method == 'POST':
        # Load the ML model from disk
        

        # Get the input values from the form
        Gender = int(request.POST.get('Gender'))
        Married = int(request.POST.get('Married'))
        Dependents = int(request.POST.get('Dependents'))
        Education = int(request.POST.get('Education'))
        Self_Employed = int(request.POST.get('Self_Employed'))
        ApplicantIncome = float(request.POST.get('ApplicantIncome'))
        CoapplicantIncome = float(request.POST.get('CoapplicantIncome'))
        LoanAmount = float(request.POST.get('LoanAmount'))
        Loan_Amount_Term = float(request.POST.get('Loan_Amount_Term'))
        Credit_History = int(request.POST.get('Credit_History'))
        Property_Area = int(request.POST.get('Property_Area'))
        

        data = pd.DataFrame({
            'Gender': [Gender],
            'Married': [Married],
            'Dependents': [Dependents],
            'Education': [Education],
            'Self_Employed': [Self_Employed],
            'ApplicantIncome': [ApplicantIncome],
            'CoapplicantIncome': [CoapplicantIncome],
            'LoanAmount': [LoanAmount],
            'Loan_Amount_Term': [Loan_Amount_Term],
            'Credit_History': [Credit_History],
            'Property_Area': [Property_Area]
         })
        
        # Make prediction on the input data
        prediction = model.predict(data)

        # Map the prediction to a readable value
        if prediction == 0:
            prediction = 'Approved'
        else:
            prediction = 'Not Approved'
        return render(request, 'main.html', {'prediction': prediction})
        
    # Render the loan prediction form template for GET requests
    return render(request, 'main.html')
    


 
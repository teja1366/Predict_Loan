# Predict_Loan
Predicting Loan Status By Using ML.
After Visulaize the data and find a good model to the problem , next we have to deploy the model.
This can be done by using flask, django or any other frameworks.
Here, i've done the deployment by using Django Framework.
After Creating a Newapp Called "predictapp", add a new file to that as urls.py
And  add the newapp name to the INSTALLED_APPS in settings.py
Then i've added the files  regarding with that and make sure you have to add the urls.py of predict app to the main urls.py
Create a new folder called templates and add new file in it called as main.html, and create the page.
Add like this 'DIRS': [BASE_DIR / 'templates'], in templates in settins.py
create a two folders separately called as NoteBooks to save the model which given high accuracy, and SavedModels as another folder where we save the model by using dump.

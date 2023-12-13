from flask_wtf import FlaskForm
from wtforms import SelectField,IntegerField,SubmitField
from wtforms.validators import DataRequired

class Inputform(FlaskForm):
    modelselection = SelectField('select Model', choices = [('LogisticRegression', 'Logistic Regression'),('DecisionTreeClassifier', 'Decision Tree') ,('SVC', 'SVM'),('KNeighborsClassifier', 'KNN')],coerce=str)  
    ApplicantIncome = IntegerField('Applicant income',validators=[DataRequired()])
    CoapplicantIncome = IntegerField('Coapplicant Income',validators=[DataRequired()])
    LoanAmount = IntegerField('Loan Amount', validators=[DataRequired()])
    Loan_Amount_Term = IntegerField('Loan Amount Term (in months)',validators=[DataRequired()])
    Credit_History = IntegerField('Credit History',validators=[DataRequired()])

    Gender = SelectField('select Gender', choices = [('Male', 'Male'),('female', 'Female')],coerce=str)  
    Martial_Status = SelectField('Martial_Status', choices = [('Married_Yes','Yes'),('Married_No','No')])  
    Dependents = SelectField('Dependents', choices = [('Dependents_0','0'),('Dependents_1','1'),('Dependents_2','2'),('Dependents_3+','3+')])  
    Education = SelectField('select Education', choices = [('Education_Graduate','Graduate'),('Education_Not Graduate', 'Not Graduate')])  
    Self_Employed = SelectField('Self Employed', choices = [('Self_Employed_Yes','Yes'),('Self_Employed_No','No')])  
    property_Area = SelectField('property Area',choices=[('property_Area_Rural','Rural'),('property_Area_Semiurban','Semiurban'),('property_Area_Urban','Urban')])

    submit = SubmitField("Submit")
   

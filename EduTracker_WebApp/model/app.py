import pickle
from flask import Flask, render_template, request
import numpy as np
import pandas as pd

app = Flask(__name__)
def prediction(lst):
    filename = r'model\best_model.pkl'
    with open(filename,'rb') as file:
        model = pickle.load(file)
    lst = pd.DataFrame([lst], columns=['Age', 'Gender', 'Ethnicity', 'ParentalEducation', 'StudyTimeWeekly', 'Absences', 'Tutoring', 'ParentalSupport', 'Extracurricular', 'Sports', 'Music', 'Volunteering'])
    pred_value = model.predict(lst)
    print(int(pred_value[0][0]))
    return int(pred_value[0][0])

@app.route('/', methods=['POST', 'GET'])
def index():
    pred = 0
    if request.method == 'POST':
         # request all the input fields
        age = int(request.form['age'])
        studytime = float(request.form['studytimeweekly'])
        absences = int(request.form['absences'])
        gender = int(request.form['gender'])
        ethnicity = int(request.form['ethnicity'])
        extracurricular = int(request.form['extracurricular'])
        sports = int(request.form['sports'])
        music = int(request.form['music'])
        volunteering = int(request.form['volunteering'])
        parentaleductaion = int(request.form['parentaleducation'])
        parentalsupport = int(request.form['parentalsupport'])
        tutoring = int(request.form['tutoring'])

        feature_list = []

        feature_list.append(age)
        feature_list.append(gender)
        feature_list.append(ethnicity)
        feature_list.append(parentaleductaion)
        feature_list.append(studytime)
        feature_list.append(absences)
        feature_list.append(tutoring)
        feature_list.append(parentalsupport)
        feature_list.append(extracurricular)
        feature_list.append(sports)
        feature_list.append(music)
        feature_list.append(volunteering)
        print(feature_list)
        
        tutoring_list = ['no', 'yes']
        volunteering_list = ['no', 'yes']
        ethnicity_list = ['Caucasian','African American','Asian', 'Other']
        parentaleductaion_list = ['None','High School', 'Some College', 'Bachelors', 'Higher']
        gender_list = ['Male', 'Female']
        parentalsupport_list = ['None', 'Low', 'Moderate', 'High', 'Very High']
        extracurricular_list = ['no', 'yes']
        sports_list = ['no', 'yes']
        music_list = ['no', 'yes']



        # def traverse_list(lst, value):
        #     for item in lst:
        #         if item == value:
        #             feature_list.append(1)
        #         else:
        #             feature_list.append(0)

        # traverse_list(gender_list, gender)
        # traverse_list(ethnicity_list, ethnicity)
        # traverse_list(tutoring_list, tutoring)
        # traverse_list(volunteering_list, volunteering)
        # traverse_list(parentaleductaion_list, parentaleductaion)
        # traverse_list(parentalsupport_list, parentalsupport)
        # traverse_list(extracurricular_list, extracurricular)
        # traverse_list(sports_list, sports)
        # traverse_list(music_list, music)
        
        #pred = prediction(pd.DataFrame([feature_list], columns=['Age', 'Gender', 'Ethnicity', 'ParentalEducation', 'StudyTimeWeekly', 'Absences', 'Tutoring', 'ParentalSupport', 'Extracurricular', 'Sports', 'Music', 'Volunteering']))
        pred = prediction(feature_list)


    return render_template("index.html", pred = int(pred))


if __name__ == '__main__':
    app.run(debug=False)


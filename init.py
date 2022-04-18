from flask import Flask, render_template, request
from StagingPythonFiles import BladderStaging, BreastStaging, ColonStaging, LungStaging, ProstateStaging
#import mysql.connector

patientID = 1
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/aboutMe')
def aboutMe():
    return render_template('aboutMe.html')


@app.route('/bladder', methods=['GET', 'POST'])
def bladder():
    if request.method == 'POST':
        print(request.form)
        requestDict = request.form
        stage = BladderStaging.getValues(requestDict)
        BladderStaging.input_into_database(requestDict,stage[1])
        return render_template('bladder.html',toStage=stage[0],stage=stage[1])

    return render_template('bladder.html')


@app.route('/breast', methods=['GET', 'POST'])
def breast():
    # heh heh boobs
    if request.method == 'POST':
        # print(request.form)
        requestDict = request.form
        stage = BreastStaging.getValues(requestDict)
        BreastStaging.input_into_database(requestDict, stage[1])
        return render_template('breast.html',toStage=stage[0],stage=stage[1])
    return render_template('breast.html')


@app.route('/colon', methods=['GET', 'POST'])
def colon():
    if request.method == 'POST':
        # print(request.form)
        requestDict = request.form
        stage = ColonStaging.getValues(requestDict)
        ColonStaging.input_into_database(requestDict, stage[1])
        return render_template('colon.html',toStage=stage[0],stage=stage[1])
    return render_template('colon.html')


@app.route('/lung', methods=['GET', 'POST'])
def lung():
    # have you or a loved one been diagnosed with mesothelioma
    if request.method == 'POST':
        # print(request.form)
        requestDict = request.form
        stage = LungStaging.getValues(requestDict)
        LungStaging.input_into_database(requestDict, stage[1])
        return render_template('lung.html',toStage=stage[0],stage=stage[1])
    return render_template('lung.html')


@app.route('/prostate', methods=['GET', 'POST'])
def prostate():
    # the forbidden scrunchy
    if request.method == 'POST':
        print(request.form)
        requestDict = request.form
        stage = ProstateStaging.getValues(requestDict)
        ProstateStaging.input_into_database(requestDict, stage[1])
        return render_template('prostate.html',toStage=stage[0],stage=stage[1])
    return render_template('prostate.html')

@app.route('/displayAll',methods=['GET','POST'])
def displayAll():
    # mydb = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="R5eu12o$"
    # )
    # if mydb.is_connected():
    #     print("Connected")
    # else:
    #     print("Not connected")
    # mycursor = mydb.cursor()
    # mycursor.execute("use capstone")
    return render_template('displayAll.html')
if __name__ == '__main__':
    app.run()

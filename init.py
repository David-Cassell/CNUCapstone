from flask import Flask, render_template, request
from StagingPythonFiles import BladderStaging, BreastStaging, ColonStaging, LungStaging, ProstateStaging
import mysql.connector

patientID = 1
app = Flask(__name__)

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R5eu12o$",
        database="capstone"
    )

mycursor = mydb.cursor(buffered=True)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/aboutMe')
def aboutMe():
    return render_template('aboutMe.html')


@app.route('/bladder', methods=['GET', 'POST'])
def bladder():
    if request.method == 'POST':
        # print(request.form)
        requestDict = request.form
        stage = BladderStaging.getValues(requestDict)
        BladderStaging.input_into_database(requestDict, stage[1])
        return render_template('bladder.html', toStage=stage[0], stage=stage[1])

    return render_template('bladder.html')


@app.route('/breast', methods=['GET', 'POST'])
def breast():

    if request.method == 'POST':
        # print(request.form)
        requestDict = request.form
        stage = BreastStaging.getValues(requestDict)
        BreastStaging.input_into_database(requestDict, stage[1])
        return render_template('breast.html', toStage=stage[0], stage=stage[1])
    return render_template('breast.html')


@app.route('/colon', methods=['GET', 'POST'])
def colon():
    if request.method == 'POST':
        # print(request.form)
        requestDict = request.form
        stage = ColonStaging.getValues(requestDict)
        ColonStaging.input_into_database(requestDict, stage[1])
        return render_template('colon.html', toStage=stage[0], stage=stage[1])
    return render_template('colon.html')


@app.route('/lung', methods=['GET', 'POST'])
def lung():

    if request.method == 'POST':
        # print(request.form)
        requestDict = request.form
        stage = LungStaging.getValues(requestDict)
        LungStaging.input_into_database(requestDict, stage[1])
        return render_template('lung.html', toStage=stage[0], stage=stage[1])
    return render_template('lung.html')


@app.route('/prostate', methods=['GET', 'POST'])
def prostate():

    if request.method == 'POST':
        # print(request.form)
        requestDict = request.form
        stage = ProstateStaging.getValues(requestDict)
        ProstateStaging.input_into_database(requestDict, stage[1])
        return render_template('prostate.html', toStage=stage[0], stage=stage[1])
    return render_template('prostate.html')


@app.route('/displayAll', methods=['GET', 'POST'])
def displayAll():
    # https://stackoverflow.com/questions/45558349/flask-display-database-from-python-to-html was where i got the idea
    # to put this in the table this way

    mycursor.execute("Select patient.pID, patient.pGender, patient.hospitalName, patient.hospitalAddress, "
                     "bladder.bladderClass, bladder.bladderTValue, bladder.bladderMets, bladder.bladderLymph, "
                     "bladder.bladderStage from patient RIGHT JOIN Bladder ON patient.pID = bladder.patientID")
    Bladder_data = mycursor.fetchall()

    mycursor.execute("Select patient.pID, patient.pGender, patient.hospitalName, patient.hospitalAddress, "
                     "prostate.prostateClass, prostate.prostateTValue, prostate.prostateMets, prostate.prostateLymph, "
                     "prostate.prostatePSA, prostate.prostateGleason, prostate.prostateStage from patient RIGHT JOIN "
                     "Prostate ON patient.pID = prostate.patientID")
    Prostate_data = mycursor.fetchall()

    mycursor.execute("Select patient.pID, patient.pGender, patient.hospitalName, patient.hospitalAddress, "
                     "lung.lungClass, lung.lungTValue, lung.lungMets, lung.lungLymph, "
                     "lung.lungStage from patient RIGHT JOIN Lung ON patient.pID = lung.patientID")
    Lung_data = mycursor.fetchall()

    mycursor.execute("Select patient.pID, patient.pGender, patient.hospitalName, patient.hospitalAddress, "
                     "breast.breastClass, breast.breastTValue, breast.breastGrade, breast.breastMets, "
                     "breast.breastLymph, breast.breastER, breast.breastHER2, breast.breastPER, breast.breastStage "
                     "from patient RIGHT JOIN Breast ON patient.pID = breast.patientID")
    Breast_data = mycursor.fetchall()

    mycursor.execute("Select patient.pID, patient.pGender, patient.hospitalName, patient.hospitalAddress, "
                     "colon.colonClass, colon.colonTValue, colon.colonMets, colon.colonLymph, "
                     "colon.colonStage from patient RIGHT JOIN Colon ON patient.pID = colon.patientID")
    Colon_data = mycursor.fetchall()

    return render_template('displayAll.html', Bladder_data=Bladder_data, Prostate_data=Prostate_data,
                           Lung_data=Lung_data, Breast_data=Breast_data, Colon_data=Colon_data)


if __name__ == '__main__':
    app.run()

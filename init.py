from flask import Flask, render_template, request
from StagingPythonFiles import BladderStaging, BreastStaging, ColonStaging, LungStaging, ProstateStaging

app = Flask(__name__)

stagingDictionary = {}


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
        return render_template('bladder.html',toStage=stage[0],stage=stage[1])

    return render_template('bladder.html')


@app.route('/breast', methods=['GET', 'POST'])
def breast():
    if request.method == 'POST':
        # print(request.form)
        requestDict = request.form
        stage = BreastStaging.getValues(requestDict)
        return render_template('breast.html',toStage=stage[0],stage=stage[1])
    return render_template('breast.html')


@app.route('/colon', methods=['GET', 'POST'])
def colon():
    if request.method == 'POST':
        # print(request.form)
        requestDict = request.form
        stage = ColonStaging.getValues(requestDict)
        return render_template('colon.html',toStage=stage[0],stage=stage[1])
    return render_template('colon.html')


@app.route('/lung', methods=['GET', 'POST'])
def lung():
    if request.method == 'POST':
        # print(request.form)
        requestDict = request.form
        stage = LungStaging.getValues(requestDict)
        return render_template('lung.html',toStage=stage[0],stage=stage[1])
    return render_template('lung.html')


@app.route('/prostate', methods=['GET', 'POST'])
def prostate():
    if request.method == 'POST':
        print(request.form)
        requestDict = request.form
        stage = ProstateStaging.getValues(requestDict)
        print (stage[1])
        return render_template('prostate.html',toStage=stage[0],stage=stage[1])
    return render_template('prostate.html')


if __name__ == '__main__':
    app.run()

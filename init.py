from flask import Flask, render_template, request

import StagingPythonFiles.BladderStaging

app = Flask(__name__)

stagingDictionary = {}


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/aboutMe')
def aboutMe():
    return render_template('aboutMe.html')


@app.route('/bladder', methods=['GET','POST'])
def bladder():
    if request.method == 'POST':
        StagingPythonFiles.BladderStaging.getValues()
        return render_template('base.html')

    return render_template('bladder.html')


@app.route('/breast', methods=['POST'])
def breast():
    return render_template('breast.html')


@app.route('/colon', methods=['POST'])
def colon():
    return render_template('colon.html')


@app.route('/lung', methods=['POST'])
def lung():
    return render_template('lung.html')


@app.route('/prostate', methods=['POST'])
def prostate():
    return render_template('prostate.html')


if __name__ == '__main__':
    app.run()

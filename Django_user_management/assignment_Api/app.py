from flask import Flask, render_template, request
import mergeOperations
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.form['upload-file']
        print(file)
        do = mergeOperations.DataOperations()
        do.addData(file)
        data = do.joinData('/','Customer Id')
       
        return render_template('data.html', data=data.to_html())


if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=8001)

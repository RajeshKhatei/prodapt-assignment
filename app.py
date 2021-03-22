from flask import Flask

from config.constant import STATIC_FOLDER

from os import listdir
from os.path import isfile, join
import csv

app = Flask(__name__)


@app.route('/')
def index():
    files_list = [f for f in listdir('static') if isfile(join('static', f))]

    csv_headings = []
    output = []

    for f in files_list:
        with open(STATIC_FOLDER+'/'+f, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    csv_headings.append(row)
                output.append(row)

    with open('output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(output)
    return "Output.csv file generated"


if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0")


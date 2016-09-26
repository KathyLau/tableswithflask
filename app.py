from flask import Flask, render_template
import utils.occu

app = Flask(__name__)

@app.route("/")
def root():
    d = utils.occu.create_dictionary('occupations.csv')
    return render_template("template.html", foo="Occupations", occuDict=d, randjob = utils.occu.chooser(d))

if __name__ == '__main__':
    app.run(debug=True)

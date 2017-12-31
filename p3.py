from flask import Flask, render_template,request

from p import *
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
		z=([float(x) for x in request.form.values()])
		z=[z[x:x+4] for x in range(0,12,4)]
		return render_template('a.html')+main(z)
	return render_template('a.html')
     

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True)
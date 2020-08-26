from flask import Flask,render_template,request
import os
import joblib
app = Flask(__name__)
l = list()
@app.route('/')
def index():
	return render_template('index.html')


@app.route('/',methods=['POST'])
def getData():
	sepal_length = request.form['sepal_length']
	sepal_width = request.form['sepal_width']
	petal_length = request.form['petal_length']
	petal_width = request.form['petal_width']

	lb = [sepal_length,sepal_width,petal_length,petal_width]
	l.append(lb)
	load = joblib.load('finalized_model.pkl')  
	# Use the loaded model to make predictions 
	result = list(load.predict(l))
	ans = ""
	n = len(result)
	print(result[n-1])

	if(result[n-1] == 0):
		ans = "Iris Setosa"
	elif(result[n-1] == 1):
		ans = "Iris Versicolour"
	else:
		ans = "Iris Virginica"
	print(result)
	return render_template('index.html',s_l = sepal_length, s_w = sepal_width,p_l = petal_length,p_w = petal_width,r = ans)

if __name__ == '__main__':
   app.run(debug=True)
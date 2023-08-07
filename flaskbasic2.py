from flask import  Flask , request, render_template , jsonify
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def math_ops():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1= int(request.form['num1'])
        num2= int(request.form['num2'])
        if operation == 'add':
            r = num1 + num2 
            result = "The sum of "  +  str(num1)   +  'and' +   str(num2) +   "is "  +  str(r)
            # return render_template('result.html', result = result)
        elif operation == 'substract' :
            r = abs(num1 - num2)
            result = "The substract of " +  str(num1) +  'and' + str(num2) +  "is "  + str(r)
        elif operation == 'multiply':
            r = num1 * num2 
            result = "The multiply of " +  str(num1) +  'and' + str(num2) +  "is "  + str(r)
        elif operation == 'divided':
            r= num1 / num2 
            result = "the divide of " + str(num1) + 'and' + str(num2) + "is" + str(r)
        else:
            result= operation + "it is not a arithmatic operator and not supported"
        
        return render_template('result.html', result = result)


@app.route('/mathwithpostman',methods=['POST'])
def math_withjson():
    #if (request.method == 'POST'):
        operation = request.json['operation']
        num1= int(request.json['num1'])
        num2= int(request.json['num2'])
        if operation == 'add':
            r = num1 + num2 
            result = "The sum of "  +  str(num1)   +  'and' +   str(num2) +   "is "  +  str(r)
            print("result", result)
            # return render_template('result.html', result = result)
        elif operation == 'substract' :
            r = abs(num1 - num2)
            result = "The substract of " +  str(num1) +  'and' + str(num2) +  "is "  + str(r)
        elif operation == 'multiply':
            r = num1 * num2 
            result = "The multiply of " +  str(num1) +  'and' + str(num2) +  "is "  + str(r)
        elif operation == 'divided':
            r= num1 / num2 
            result = "the divide of " + str(num1) + 'and' + str(num2) + "is" + str(r)
        else:
            result= operation + "it is not a arithmatic operator and not supported"
        return jsonify(result)

@app.route("/")
def hello_world():
    return "<h1>hello, world!</git h1>"
    
@app.route("/test")
def test2():
    data = request.args.get('x')
    return "this is data input from my url {}".format(data)

@app.route("/login")
def test3():
     return "<h1>logeed in!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

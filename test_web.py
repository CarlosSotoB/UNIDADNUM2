from perimetro import perimeter_trapeze
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def home()-> '302':
    return redirect('/entry')


@app.route('/entry')
def go_entry()-> 'html':
    return render_template('entry.html',
                           the_title='Welcome to the form')


@app.route('/calculate', methods=['POST'])
def calculate()-> 'html':
    bm = float(request.form['bm'])
    b = float(request.form['b'])
    a = float(request.form['a'])
    c = float(request.form['c'])

    result = perimeter_trapeze(bm,b,a,c)
    title = "Trapeze perimeter result"
    return render_template('result.html', the_bm=bm, the_b=b, the_a=a, the_c=c, the_result=result, the_title=title)


app.run(debug=True)
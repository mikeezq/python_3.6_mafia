from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target = request.form.get('target')
        result = [target.upper()] * 4
        return render_template('index.html', result=result)
    return render_template('index.html')


@app.route('/redirect', methods=['POST'])
def redirect_to_page():
    return redirect('http://localhost:8080/')


if __name__ == '__main__':
    app.run(debug=True)
import os

from flask import Flask, render_template, request, redirect
import joblib

from model.category_model import topn, get_model_tokenizer

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target = request.form.get('target')
        result = topn(target, tokenizer, model, le, codes_dict)
        return render_template('index.html', result=result)
    return render_template('index.html', result=[''])


@app.route('/redirect', methods=['POST'])
def redirect_to_page():
    return redirect('http://localhost:8080/superset/dashboard/1/?native_filters_key=GR_X6YsqAFAEuAfo_hiEGsL_TfIw3PlBOEBAZtDD9q1UeCcuiQKQmHbSflhydIjy')


if __name__ == '__main__':
    curdir = os.getcwd()
    model, tokenizer = get_model_tokenizer(os.path.join(curdir, '../../model_data/modelg.pt'))
    le = joblib.load(os.path.join(curdir, '../../model_data/le.pkl'))
    codes_dict = joblib.load(os.path.join(curdir, '../../model_data/codes_dict.pkl'))
    app.run(debug=True)

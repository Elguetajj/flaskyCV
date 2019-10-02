from flask import Flask, render_template, url_for
import yaml

app = Flask(__name__)

with open('data.yml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

print(data)

@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html', data=data)

@app.route('/education')
def education():
    return render_template('education.html', data=data)

@app.route('/skills')
def skills():
    return render_template('skills.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

posts=[
  {
	'author':'Wakhanu Satwinder',
	'title':'Blog Post 1',
	'content':'First post Content',
	'date_posted':'October 28th 2019'
  },
  {
	'author':'Sharon Nyangasi',
	'title':'Blog Post 2',
	'content':'Second post Content',
	'date_posted':'October 28th 2019'
  }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='about')


if __name__ == '__main__':
        app.run(debug=True)
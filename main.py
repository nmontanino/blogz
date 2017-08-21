from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:passwordlol@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(420))


    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/')
def index():
    return redirect('/blog')

@app.route('/blog')
def blog():
    
    posts = Blog.query.all()
    return render_template('blog.html', posts=posts, title='Blog')

@app.route('/newpost', methods=['POST', 'GET'])
def new_post():
    
    if request.method == 'POST':
        title = request.form['blog-title']
        body = request.form['blog-entry']

        new_entry = Blog(title, body)
        
        db.session.add(new_entry)
        db.session.commit()
        return redirect('/blog')
    else:
        return render_template('newpost.html', title='New Entry')

if  __name__ == "__main__":
    app.run()
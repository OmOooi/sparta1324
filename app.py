from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()




# @app.route('/')
# def index():
#     post_list = Post.query.all()
#     return render_template('index.html', data=post_list)

@app.route("/post_add")
def post_add():
    return render_template('post_add.html')

@app.route("/post_add_button")
def post_add_button():
    # form에서 보낸 데이터 받아오기
    username_receive = request.args.get("username")
    title_receive = request.args.get("title")
    content_receive = request.args.get("content")

    #데이터를 db에저장하기 
    post = Post(username = username_receive, title= title_receive, content=content_receive)
    db.session.add(post)
    db.session.commit()
    return render_template('index.html')




# @app.route("/post")
# def post():
#     return render_template("post.html")


# 댓글 추가
# @app.route('post_add_button')
# def post_add_button():
#     comment_add_username_receive = request.args.get("comment_add_username")
#     comment_add_input_receive = request.args.get("comment_add_inpute")
#     song_comment = Song_comment(comment_add_username=comment_add_username_receive, comment_add_input = comment_add_input_receive )
#     db.session.add(song_comment)
#     db.session.commit()
#     return render_template('post.html')



if __name__ == "__main__":
    app.run(debug=True, port=8080)
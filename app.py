from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# MySQL 데이터베이스 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql 데이터'

# SQLAlchemy 초기화
db = SQLAlchemy(app)

# 모델 정의
class Song(db.Model):
    username = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route("/post_add")
def post_add():
    # form에서 보낸 데이터 받아오기
    username_receive = request.args.get('username')
    title_receive = request.args.get('title')
    content_receive = request.args.get('content')

    #데이터를 db에저장하기 
    song = song(username = username_receive, title= title_receive, content=content_receive )
    db.session.add(song)
    db.session.comit()
    return render_template("post_add.html")

@app.route("/post")
def post():
    post_n = Song.query.all()
    return render_template("post.html", data=post_n)



if __name__ == "__main__":
    app.run(debug=True, port=8080)
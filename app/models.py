from . import db

class Source:
    '''Defines source objects'''

    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description


class Article:
    '''Article class to define article objects'''

    def __init__(self,id,title,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'




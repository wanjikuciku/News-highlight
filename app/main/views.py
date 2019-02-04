from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_articles
from ..models import News,Articles

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'News Highlight'
    general_news = get_news('general')
    business_news = get_news('business')
    sports_news = get_news('sports')
    technology_news = get_news('technology')
    return render_template('index.html',title = title,general = general_news,business = business_news, sports = sports_news, technology = technology_news )


@main.route('articles/<id>')
def articles(id):
    '''
    View a specific source page and its articles
    '''
    articles = get_articles(id)
    title = f'{id}'
    return render_template('articles.html',id = id, articles = articles)

"""
Routes and views for the bottle application.
"""

from bottle import route, view


@route('/')
@route('/home')
@view('Start')
def home():
    """Renders the home page."""
    return dict(
        title1='Данный сайт подготовлен для выполнения задания по учебной практике.',
        title2='Сайт предназначен для построения и нахождения крайчайших путей с помощью различных алгоритмов.'
    )
@route('/index')
@view('index')
def home():
    """Renders the home page."""
    return dict(

    )

@route('/Ewoks')
@view('Ewoks')
def contact():
    """Renders the contact page."""
    return dict(
        title='Ewoks'

    )

@route('/Porgs')
@view('Porgs')
def about():
    """Renders the about page."""
    return dict(
        title='Porgs'

    )
@route('/Wookiee')
@view('Wookiee')
def about():
    """Renders the about page."""
    return dict(
        title='Wookiee'

    )

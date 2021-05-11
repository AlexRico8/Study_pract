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
@route('/Main')
@view('Main')
def home():
    """Renders the home page."""
    return dict(
        title='Алгоритмы:',
        title1='Алгоритм Прима',
        title2='Алгоритм Дейкстра',
        title3='Алгоритм Флойда'
    )

@route('/Prima')
@view('Prima')
def contact():
    """Renders the contact page."""
    return dict(
        title='Алгоритм Прима'

    )

@route('/Dextra')
@view('Dextra')
def about():
    """Renders the about page."""
    return dict(
        title='Алгоритм Дейкстра'

    )
@route('/Floid')
@view('Floid')
def about():
    """Renders the about page."""
    return dict(
        title='Алгоритм Флойда'

    )

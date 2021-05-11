"""
Routes and views for the bottle application.
"""

from bottle import route, view


@route('/')
@route('/home')
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

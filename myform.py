from bottle import post, request
import re
@post('/Main', method='post')
def my_form():
    Matriza = request.forms.get('GetValue')
    
from bottle import post, request
import re
@post('/index', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    qwer =  request.forms.get('QUEST')
    if qwer=="" or  mail=="":
         return "Not all fields are filled "
    else:
        match = re.search(r'([@]mail[.]ru)', mail)
        if match!=None:
            return "Thanks! The answer will be sent to the mail %s" % mail
        else:
            return "This mail doesn't exist %s"% mail
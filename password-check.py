import string
 
def checkio(data):
    su=string.uppercase
    sl=string.lowercase
    di=string.digits
    pull=[]
    a=0
    b=0
    c=0
    for item in data:
        if item in su:
            a+=1
        elif item in sl:
            b+=1
        elif item in di:
            c+=1
    if len(data)>=10 and a>0 and b>0 and c>0:
        return True
    else:
        False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"

import string
 
def checkio(text):
    arr={}
    test=[]
    sl=string.lowercase
    text=text.lower()
#initializing the empty dictionary
    for l in text:
        if l in sl:
            arr[l]=0
        else:
            continue
#counting each letter frequency            
    for letter in text:
        if letter in sl: 
            number=text.count(letter)
            arr[letter]+=1
        else:
            continue
#__________________________________________________1START_CODE
    a=arr.items()
    b=a[:]
    a.sort(cmp=lambda x,y: cmp(x[1], y[1]))
    if a[0][1]!=a[-1][1]:
#__________________________________________________2START_CODE        
        for item in a:
            if item[1]==a[-1][1]:
                test.append(item)
            else:
                continue
        test.sort()
        return test[0][0]
#__________________________________________________2END_CODE            
    else:
        b.sort()
        return b[0][0]
#__________________________________________________1END_CODE
 
 
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")

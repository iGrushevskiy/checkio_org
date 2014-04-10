FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
 
def checkio(number):
    #dictionary for the first ten
    ten={}
    ten2={}
    ten3={}
     
    #values for counters
    m1=1
    m2=10
    m3=2
     
    #result value for the 2 digit values
    dig2=[]
     
    #result value for the 3 digit values
    dig3=[]
     
    #populating ten dictionary with values
    for item in FIRST_TEN:
        ten[item]=m1
        m1+=1
    #here we have {'seven': 7, 'nine': 9, 'six': 6, 'three': 3, 'two': 2, 'four': 4, 'five': 5, 'eight': 8, 'one': 1}
    #so need to sort, getting items pair
    a=ten.items()
    #[('seven', 7), ('nine', 9), ('six', 6), ('three', 3), ('two', 2), ('four', 4), ('five', 5), ('eight', 8), ('one', 1)]
    b=a[:]
    b.sort(cmp=lambda x,y: cmp(x[1], y[1]))
    #[('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)]
     
    #doing the same for the second ten dictionary
    for item in SECOND_TEN:
        ten2[item]=m2
        m2+=1
    c=ten2.items()
    d=c[:]
    d.sort(cmp=lambda x,y: cmp(x[1], y[1]))
    #[('ten', 10), ('eleven', 11), ('twelve', 12), ('thirteen', 13), ('fourteen', 14), ('fifteen', 15), ('sixteen', 16), ('seventeen', 17), ('eighteen', 18), ('nineteen', 19)]
     
    #doing similar thins for other hundreds
    for item in OTHER_TENS:
        ten3[item]=m3
        m3+=1
    e=ten3.items()
    f=e[:]
    f.sort(cmp=lambda x,y: cmp(x[1], y[1]))    
    #[('twenty', 2), ('thirty', 3), ('forty', 4), ('fifty', 5), ('sixty', 6), ('seventy', 7), ('eighty', 8), ('ninety', 9)]
     
    if number<10:
        for item in b:
            if item[1]==number:
                return item[0]
            else:
                continue
             
    elif number>=10 and number<20:
        for item in d:
            if item[1]==number:
                return item[0]
            else:
                continue
    else:
        number=str(number)
#20-99
        if len(number)==2:
            for item in f:
                if item[1]==int(number[0]):
                    dig2.append(item[0])
                else:
                    continue
#as a result here we should have 2dig string value with the first word(for the first digit in number)
#for example, in case of number 21 for the 2dig will be appended 'twenty'
            for item in b:
                if item[1]==int(number[1]):
                    dig2.append(item[0])
                    return ' '.join(dig2)
                #checking excaptional case whether the last symbol is 0 so 
                #return just 1st digit value and break the loop
                elif int(number[1])==0:
                    return ' '.join(dig2)
                    break
                else:
                    continue
 
#100-999
        elif len(number)==3:
            #creating temporary var for the exceptional case
            last2dig=number[-2]+number[-1]
         
#---START COPY FROM THE FIRST AND LAST TENS-------            
            if int(last2dig)<10:
                for item in b:
                    if item[1]==int(number[0]):
                        dig3.append(item[0])
                    else:
                        continue
                for item in b:
                    if item[1]==int(last2dig):
                        dig3.append(HUNDRED)
                        dig3.append(item[0])
                        return ' '.join(dig3)#.append(item[0])
                    elif int(last2dig)==0:
                        dig3.append(HUNDRED)
                        return ' '.join(dig3)
                        break
                    else:
                        continue
#---1.FINISHED DEBUGGING            
            elif int(last2dig)>=10 and int(last2dig)<20:
                for item in b:
                    if item[1]==int(number[0]):
                        dig3.append(item[0])
                    else:
                        continue
                for item in d:
                    if item[1]==int(last2dig):
                        dig3.append(HUNDRED)
                        dig3.append(item[0])
                        return ' '.join(dig3)#.append(item[0])
                    else:
                        continue
#---2.FINISHED DEBUGGING
 
 
 
 
#---END COPY FROM THE FIRST AND LAST TENS------
            else:
                for item in b:
                    if item[1]==int(number[0]):
                        dig3.append(item[0])
                    else:
                        continue
#adding HUNDRED WORD to exclude case without hundred word like this ['two', 'thirty', 'four']
                dig3.append(HUNDRED)
#---START COPY FROM THE 2 DIGIT SOLUTION
                for item in f:
                    if item[1]==int(number[1]):
                        dig3.append(item[0])
                    else:
                        continue
#as a result here we should have 2dig string value with the first word(for the first digit in number)
#for example, in case of number 21 for the 2dig will be appended 'twenty'
                for item in b:
                    if item[1]==int(number[2]):
                        dig3.append(item[0])
                        return ' '.join(dig3)
                #checking excaptional case whether the last symbol is 0 so 
                #return just 1st digit value and break the loop
                    elif int(number[2])==0:
                        return ' '.join(dig3)
                        break
                    else:
                        continue
#---END COPY FROM THE 2 DIGIT SOLUTION                    
 
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"

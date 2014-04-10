FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
'''Symbols are placed from left to right in order of value, starting with the largest.
However, in a few specific cases, to avoid FOUR characters being repeated in succession (such as IIII or XXXX) 
these can be reduced using subtractive notation as follows:
a)the numeral 'I' can be placed before 'V' and 'X' to make 4 units ('IV') and 9 units ('IX' respectively)
b)'X' can be placed before 'L' and 'C' to make 40 ('XL') and 90 ('XC' respectively)
c)'C' can be placed before 'D' and 'M' to make 400 ('CD') and 900 ('CM') according to the same pattern'''
 
 
def checkio(number):
    #1,2,3,4,5,6,7,8,9
    roman={'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9}
    #10,20,40,50,60,70,80,90
    roman_ten={'X': 1, 'XX': 2, 'XXX': 3, 'XL': 4, 'L': 5, 'LX': 6, 'LXX': 7, 'LXXX': 8, 'XC': 9}
    #100,200,300,400,500,600,700,800,900
    roman_hundred={'C': 1, 'CC': 2, 'CCC': 3, 'CD': 4, 'D': 5, 'DC': 6, 'DCC': 7, 'DCCC': 8, 'CM': 9}
    #1000
    thousand={'M': 1, 'MM': 2, 'MMM': 3}
    r=[]
  
    #actually we have unsorted dictionary {'II': 2, 'IX': 9, 'VIII': 8, 'X': 10, 'V': 5, 'I': 1, 'VI': 6, 'VII': 7, 'III': 3, 'IV': 4}
    #so need to sort
    #1.Getting items pair
    a=roman.items()
    #[('II', 2), ('IX', 9), ('VIII', 8), ('X', 10), ('V', 5), ('I', 1), ('VI', 6), ('VII', 7), ('III', 3), ('IV', 4)]
    b=a[:]
    #2.Sorting
    b.sort(cmp=lambda x,y: cmp(x[1], y[1]))
    #now we have sorted data
    #[('I', 1), ('II', 2), ('III', 3), ('IV', 4), ('V', 5), ('VI', 6), ('VII', 7), ('VIII', 8), ('IX', 9), ('X', 10)]
     
    #doing the same with roman_ten
    c=roman_ten.items()
    d=c[:]
    d.sort(cmp=lambda x,y: cmp(x[1], y[1]))
     
    #doing the same with roman_hundred
    e=roman_hundred.items()
    f=e[:]
    f.sort(cmp=lambda x,y: cmp(x[1], y[1]))
     
    #doing the same with thousand
    g=thousand.items()
    h=g[:]
    h.sort(cmp=lambda x,y: cmp(x[1], y[1]))
     
#1 digits case
    if len(str(number))==1:
        for item in b:
            if item[1]==number:
                return item[0]
            else:
                continue
#2 digits case
    elif len(str(number))==2:
        number=str(number)
#dealing with the 0 index string digit
        for item in d:
            if item[1]==int(number[0]):
                r.append(item[0])
                break
            else:
                continue
#dealing with the 1 index string digit
        for item in b:
            if item[1]==int(number[1]):
                r.append(item[0])
                return ''.join(r)
            elif int(number[1])==0:
                return ''.join(r)
            else:
                continue
#3 digits case
    elif len(str(number))==3:
        number=str(number)
#dealing with the 0 index string digit
        for item in f:
            if item[1]==int(number[0]):
                r.append(item[0])
            else:
                continue
#----START COPY FROM 2 LEN DIGIT SOLUTION
#dealing with the 1 index string digit
        for item in d:
            if item[1]==int(number[1]):
                r.append(item[0])
                break
            else:
                continue
#dealing with the 2 index string digit
        for item in b:
            if item[1]==int(number[2]):
                r.append(item[0])
                return ''.join(r)
            elif int(number[2])==0:
                return ''.join(r)
            else:
                continue
#----END COPY FROM 2 LEN DIGIT SOLUTION
 
#4 digits case
    elif len(str(number))==4:
        number=str(number)
        for item in h:
            if item[1]==int(number[0]):
                r.append(item[0])
            else:
                continue
#----START COPY FROM 3 LEN DIGIT SOLUTION
 
#dealing with the 1 index string digit
        for item in f:
            if item[1]==int(number[1]):
                r.append(item[0])
            else:
                continue
#dealing with the 2 index string digit        
        for item in d:
            if item[1]==int(number[2]):
                r.append(item[0])
                break
            else:
                continue
#dealing with the last 3 index string digit
        for item in b:
            if item[1]==int(number[3]):
                r.append(item[0])
                return ''.join(r)
            elif int(number[3])==0:
                return ''.join(r)
            else:
                continue
                 
#----END COPY FROM 3 LEN DIGIT SOLUTION
         
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'

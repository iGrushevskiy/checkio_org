def checkio(data):
    a=len(data)
    if a%2==0:
        m=a/2
        data=sorted(data)
        r=float((data[m-1]+data[m])/2.0)
    else:
        m=(a/2)
        data=sorted(data)
        r=data[m]
    #replace this for solution
    return r
 
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(range(1000000)) == 499999.5, "Long."
    print("The local tests are done.")

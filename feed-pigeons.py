def pig(m):
    if m==0:
        return 0
    else:
        return pig(m-1)+m
 
def checkio(feed):
#before feeding we have
    m=0
    birds=0
    while feed>birds:
        #time starts
        m+=1
        #print 'minute',m
        birds=pig(m)
        #print 'birds',birds
        if feed<birds:
            return max(feed,birds-m)
        feed=feed-birds
        #print 'feed',feed
    return birds

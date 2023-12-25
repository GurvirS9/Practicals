def ticount():
    data = open("para.txt","r")
    tic = 0 
    ti = ["The", "the", "Is", "is"]
    for line in data:
        w = line.split()
        for word in w:
            if word in ti:
                tic = tic+1
    else:
        print("No of occurences of 'the' & 'is'", tic)

ticount()

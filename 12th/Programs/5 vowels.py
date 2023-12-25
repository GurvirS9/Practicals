def vowelcount():
    data = open("para.txt","r")
    vc = 0 
    vow = "aeiouAEIOU"
    for line in data:
        for ch in line:
            if ch in vow:
                vc = vc+1
    else:
        print("Vowel Count:", vc)

vowelcount()

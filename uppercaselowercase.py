def countstring(string):
    case={"upper":0, "lower":0}
    for j in string:
        if j.isupper():
           case["upper"]+=1
        elif j.islower():
           case["lower"]+=1
        else:
           pass
    print (string)
    print ("Upper", case["upper"])
    print ("Lower", case["lower"])

countstring("My Name is KItTy")

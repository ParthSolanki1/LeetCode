def isValid(code: str) -> bool:
    tags = []
    tag = ""
    found = False
    cdata = False
    between = 0
    end = False
    for i in range(len(code)):
        if(i < len(code)-1 and code[i:i+2] == "<!"):
            cdata = True
        elif (code[i-1:i+1] == "]>"):
            cdata = False

        if((not cdata) and code[i] == "<"):
            if(end and between == 0):
                return False
            tag += code[i]
            found = True
            between = 0
            end = code[i:i+2] == "</"
        elif(found and code[i] == ">"):
            tag += code[i]
            found = False
            tags.append(tag)
            tag=""
            between = 0
        elif(found):
            if((not code[i].isupper()) and code[i-1:i+1] != '</'):
                return False
            elif((not code[i].isupper())):
                between += 1
            tag += code[i]

    if(len(tags) % 2 == 1 or len(tags) == 0):
        return False
    i = 0
    j = 1

    while(j < len(tags)):
        if(tags[j][0:2] == "</" and tags[i][0] == "<" and tags[j][2:-1] == tags[i][1:-1]):
            tags = tags[:i] + tags[j+1:]
            i = 0
            j = 1
        else:
            i += 1
            j += 1

    return(len(tags) == 0)
    

print(isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>"))

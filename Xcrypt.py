"""

�    = "q", "w", "e", "r", "t"
字☗   = "y", "u", "i", "o", "p"
囧   = "a", "s", "d", "f", "g"
亼  = "h", "j", "k", "l"
¤  = "z", "x", "c", "v"
þß = "b", "n", "m"
▧▪  = ".", "?", ",", "!", '"', "'", ":"

"""

import random as r

randch = ["あ","한","ア","핏","글","も","ゆ","ㅂ","父","지"]

def Decrypt(text):
    dat = {'�' : ["q", "w", "e", "r", "t"],
        '字☗': ["y", "u", "i", "o", "p"],
        '囧': ["a", "s", "d", "f", "g"],
        '亼':["h", "j", "k", "l"],
        '¤':["z", "x", "c", "v"],
        'þß':["b", "n", "m"],
        '▧▪': [".", "?", ",", "!", '"', "'", ":"]}

    # ind = 0
    cont = ""
    txtd = text

    def indx(st):
        cnt = 0
        for i in st:
            if i == "◈":
                cnt +=1
            else:
                break
        return cnt

    sam = txtd
    txt = ""

    while sam != "":
        if sam[:1] in randch:
            sam = sam[1:]
        else:
            txt += sam[:1]
            sam = sam[1:]

    while txt != "":
        
        # print(cont)

        if txt[:2] == "�◈":         # ,.
            ind = indx(txt[2:9])
            ch = dat["�"]
            cont += ch[ind]
            txt = txt[2+ind:]
            continue

        if txt[:1] == " ":          # ' '
            cont += " "
            txt = txt[1:]
            continue

        if txt[:3] == "字☗◈":         # ,:.
            ind = indx(txt[3:9])
            ch = dat["字☗"]
            cont += ch[ind]
            txt = txt[3+ind:]
            continue

        elif txt[:2] == "囧◈":         # ,,.
            ind = indx(txt[2:9])
            ch = dat["囧"]
            cont += ch[ind]
            txt = txt[2+ind:]
            continue

        if txt[:2] == "亼◈":         # ,,;.
            ind = indx(txt[2:9])
            ch = dat["亼"]
            cont += ch[ind]
            txt = txt[2+ind:]
            continue

        elif txt[:2] == "¤◈":         # ,,,.
            ind = indx(txt[2:9])
            ch = dat["¤"]
            cont += ch[ind]
            txt = txt[2+ind:]
            continue

        elif txt[:3] == "▧▪◈":       # ,;,.
            ind = indx(txt[3:10])
            ch = dat["▧▪"]
            cont += ch[ind]
            txt = txt[3+ind:]
            continue

        if txt[:3] == "þß◈":        # ,,,;.
            ind = indx(txt[3:10])
            ch = dat["þß"]
            cont += ch[ind]
            txt = txt[3+ind:]
            continue

    return cont

def Encrypt(text):
    dat = [('�',"q", "w", "e", "r", "t"),
            ('字☗',"y", "u", "i", "o", "p"),
            ('囧', "a", "s", "d", "f", "g"),
            ('亼', "h", "j", "k", "l"),
            ('¤',"z", "x", "c", "v"),
            ('þß',"b", "n", "m"),
            ('▧▪',".", "?", ",", "!", '"', "'", ":")]
    
    txt = text
    res = ""
    
    for i in txt.lower():
        if i == " ":
            res += " "
        else:
            for j in range(len(dat)):
                if i in dat[j][1:]:
                    cnt = dat[j].index(i)
                    res += dat[j][0] + ("◈"*cnt)

    for _ in range(len(res)//8):
        va = r.choice(randch)
        pl = r.choice(range(0,len(res)//3,3))
        res = res[:pl] + va + res[pl:]

    return res

# with open("mystery.txt",'r',encoding="utf-8") as f:
#     enc = f.read()

# print("enc value: ")
# print(enc)

# dc = "This is the new alorithm developed for enchanced cryptography, the encrypted text contains a mix of Chinese, Japanese, Korean, Spanish and some meaningless boxes. This looks crazy isn't it!"
# print("denc value: ")
# dnc = decrypt(enc)
# print(dnc)

# print("encoded value: ")
# ec = encrypt(dnc)
# print(ec)
# print("denc value: ")
# dnc = decrypt(ec)
# print(dnc)
# print("Quality check: ")
# if enc == ec:
#     print("PASSED")



out = Encrypt("this is test enc")
print(out)
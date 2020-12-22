title = "hi there how r u"

slug = title.translate({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_"}).replace(" ", "+")
slug = slug[:15]
if slug[-1] == "+":
    slug = slug[:-1]
    print("last character is +")
    print(slug)    

print(slug)

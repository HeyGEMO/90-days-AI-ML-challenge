#unorder #mutable #no duplicate key
info = {
    "key" : "value",
    "name" : "lauda",
    "learning" : "python",
    "age" : 26,
    "is_adult" : True,
     3.0 : 85.5,
    "subject" : ["python", "c", "c++","flutter" ],
    "topic" : ("dictionary","set") #tuple
}
print(info)
print(info["name"])
print(info[3.0])
info["name"] = "GEMO"
print(info["name"])

null_dict = {}
print(null_dict)
null_dict["name"]= "hari narayan"
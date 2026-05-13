message=('Hello World')
message2=("Hello's Wrold")
message3=(""" lekhau bhabhisya afno afaile
          aaru kohi aaudaina banauna""")
print(message , message2 , message3)
print(message[0] , message[0:5] , message[5:])
print(len(message3))
print(message2.upper() , message.lower() , message3.count('i'))
print(message3.find('kohi')) #45
new_message = message.replace('World','Lauda')
print(new_message)
greeting = 'Lassan'
name = 'Gendu'
message4 = 'Hello, '+ greeting + ' ' + name
message5= '{}, {}. Welcome!'.format(greeting , name)
message6=f'{greeting}, {name.upper()}, Welcome!'
print(message4)
print(message5)
print(message6)
print(dir(name))
print(help(str))
print(help(str.lower))
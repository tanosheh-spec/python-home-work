'''  
print ('*** Form e Sbtenam ***')

first_name = input (' First Name: ') .strip () .title ()
last_name = input (' Last Name: ') .strip () .title ()
username = input (' Username: ').strip ()
password = input (' Password: ') .strip ()
address = input (' Home Address: ') .strip ()


while True :
    phone = input (' Phone Numbers (09123456789): ') .strip ()
    if phone . startswith ('09') and len(phone) == 11 and phone . isdigit ():
        break
    else:
        print ('shomare bayad adad bashad , 11 ragham bashad , ba (09) shoro shavad.')


while True :
    code_posti = input (' Code Posti: ') .strip ()
    if len (code_posti) == 10 and code_posti . isdigit ():
        break
    else:
        print (' Error! code post bayad 10 ragham bashad.')

print ( ' Etelaat shoma ba movafaghiat sabt shod. ' )
print ( 'first_name:', first_name )                
print ( 'last_name:' , last_name ) 
print ( 'username:' , username ) 
print ( 'password:' , password ) 
print ( 'phone:' , phone ) 
print ( 'address:' ,address  ) 
print ( 'code_posti:' , code_posti ) 
'''


print (' *** Forme Sbte Name: *** ')

first_name = input (' First Name: ') .strip () .title ()
last_name = input (' Last Name: ') .strip () .title ()

while True :
    mobail = input ('Mobail Numbers:') .strip () .title ()
    if mobail . startswith ('09') and len(mobail) == 11 and mobail . isdigit ():
        break
    else:
        print (' Ekhtar! somare mobail bayad adad bashad , 11 ragham bashad , ba (09) shoro shavad.')

address = input (' Home Address: ') .strip ()

while True :
    code_posti = input (' Code Posti: ') .strip ()
    if len (code_posti) == 10 and code_posti . isdigit ():
        break
    else:
        print (' Ekhtar! code posti bayad adad bashad ,  10 ragham bashad.')

username = input (' Username: ').strip ()    

while True :
    password = input (' Password: ') .strip ()
    if len (password) >= 8 :
        break
    else:
        print (' Ekhtar! password bayad 8 mored bashad adad va harf. ')

print (' Etelaat shma sabt shod. ')
print ( 'First_name:', first_name )                
print ( 'Last_name:' , last_name )        
print ( 'Mobail:' , mobail ) 
print ( ' Home Address:' , address  ) 
print ( 'Code Posti:' , code_posti )
print ( 'Username:' , username ) 
print ( 'Password:' , password ) 


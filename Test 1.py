
print('1 _____________________________________') 

age = int( input ('Enter your age:'))

if age < 18:

    print ('by by')

else:

    username = input(' Enter username:')

    password = input(' Enter passwore:')

    if username == "dark shadow " and  password == "king Arthur 7300 ":

        print('login')

    elif username != "dark shadow " and  password != "king Arthur 7300 ":

        print('joftesh ghalat')    

    elif username != "dark shadow ":
    
        print('username ghalat')    
        
    else:
         print('password ghalat')  

print('2 _____________________________________')         

masafat = float(input('masafat bar hasb KM:'))

hazine_one = 30000

one_KM = 8000

hazine_kol = hazine_one + ( masafat * hazine_one )

if masafat > 20:

    hazine_kol = hazine_kol * 0.05

print ('mablagh nahai:' , hazine_kol , 'Toman')    

print('3 _____________________________________')         

ghabz_man = int(input('masraf ra vared konid:'))

vahedi = int (input('vahed ra vared konid:'))

if ghabz_man <= 100 :

    vahedi = 1000

elif ghabz_man > 100 and vahedi <= 200: 

    vahedi = 1500 

else:

    vahedi = 2500    

mablagh_kol = ghabz_man * vahedi

print ('prdakhti:' , mablagh_kol , 'Toman')

print('4 _____________________________________')    

dama = float ( input ( 'dama chandr:'))

if dama < 0 : 

    print ('kapshan bepush')

elif 0 <= dama <= 10:

    print (' lebas garm bepush')

elif 11 <= dama <= 25:

    print ('hava motadele')   

elif dama > 25:

    print ('lebas khonak bepush')

rain = str (input( 'Aya hava baranie? (yes / no): '))    

if rain == 'yes':

    print ('chatr bebar')

print(' 5 _____________________________________') 

mojudi = float (input (' mojudi: '))

bardasht = float (input (' mablagh badasht: '))

if bardasht <= 0 :

    print ('bardasht bayad bishtar az 0 bashad!')

elif bardasht > mojudi :

    print ('mojudi kafi nist')

else:    

    mojudi_jadid = mojudi - bardasht
    print ('mojudi_jadid:' , mojudi_jadid)

    if mojudi_jadid < 100000:

        print ('hoshdar: , mojudi kamtar az 100000 shod') 

print('6 _____________________________________') 

m_kharid = float (input(' mablagh ra vared kon:'))

ersal = str (input('noe ersal: (adi / sari)'))

if ersal == 'adi' :
     
    if  m_kharid > 2000000:

        hazine = 0
    
        print('ersal raigam')

    else:

         hazine = 50000
         print ('hazine ersal:' , hazine)

         print ('')     

elif ersal == 'sari': 

    hazine = 100000
    print ('hazine ersal:' , hazine)

else :
    print('khata')


print('7 _____________________________________')    

weight = int (input( 'Enter your weight (kg):'))  

height = float (input( 'Enter your height: (m)')) 

if weight <= 0 or height <= 0 :

    print ('baya bishtar az 0 bashad!')
else: 

    bmi = weight / (height ** 2)

    print (' your BMI:' , bmi) 

    if bmi < 18.5 :
        print ('kambud vazn') 

    elif  bmi < 25 :

        print('monaseb') 

    elif  bmi < 30: 

        print ('ezafe')    

    else:

        print('chaghi')   

print('8 _____________________________________')  


age =int( input(' Enter your age:')) 

days = ["shanbe" , "1 shanbe" , "2 shanbe" , "3 shanbe " , "4 shanbe" , "5 shanbe" , "jomee"]

day = str(input(' Enter the one day:'))  


ticket = 200000

if age < 12: 

    takhfif = 50

elif age >= 60: 

    takhfif = 30

    if day  == '3 shanbe ' and takhfif < 20 :

        takhfif = 20

    final = ticket - ( ticket * takhfif / 100) 

    print ('darsad takhfif:' , takhfif , '%')

    print ('gheymat nahai:' , final , 'Toman')

print('9 _____________________________________') 

food =str (input ( ' Enter youe food:'))

tedad = int ( input( ' Enter the number your item:'))

if tedad <= 0:

    print('tedad bayad bishtar az 0 bashad')

elif food == 'pizza':

    gheymat = 250000 * tedad
    print('gheymat_kol' , gheymat ,'Toman')

    if gheymat > 500000:
        print('you have a free drink')
      
elif food == 'burger':
    
    gheymat = 180000 * tedad
    print('gheymat_kol' , gheymat ,'Toman')

    if gheymat > 500000:
            print('you have a free drink')

elif food == 'sandwich':
    
    gheymat = 120000 * tedad
    print('gheymat_kol' , gheymat ,'Toman')
    
    if gheymat > 500000:
                print('you have a free drink')
    
else: 
    print (' this food is not the menu:')

   

print('10 _____________________________________') 

password = int ( input ('Enter ypur password:'))
 
mojudi = int ( input (' mojudi:'))     

bardasht = int ( input (' bardasht:'))

if password != 1234:

    print ('password eshtebah!')

else:

    if bardasht <= 0:

        print ('mablagh bayad bishtar az 0 bashar')

    elif bardasht % 50000 and bardasht != 0:

        print (' mablagh mazrabi az 50 nist!')

    elif bardasht > mojudi:

        print(' mojudi kafi nist:') 

    else:

        j_mojudi = mojudi -  bardasht       

        print (' badasht movafagh')

        print (' j_mojudi: ' , j_mojudi , 'Tman' )


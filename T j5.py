
while True:
    user = input ('user:')
    password = input ('password:')
    if user == 'admin' and password == '12345':
        print ('login')
        break
    else:
        print ('user or password wrong!')
count = 0
while True:
    score = float (input('score :'))
    if 17 <= score <= 20:
        print ('A')
        if 17 <= score <= 18:
            print ('A-')
        elif 18 < score <= 20:
            print('A+')
    if 14 <= score < 17:
        print ('B')
        if 14 <= score <= 16:
             print ('B-')
        elif 16 <= score < 17:
             print('B+')
    if 10 <= score < 14:
        print ('C')
        if 10 <= score <= 12:
            print ('C-')
        elif 12 < score <= 14:
            print('C+')
    if 0 <= score <= 10 :    
        print ('ab ghate ')    
    count += 1
    if score == 00:
            print ('bye bye !') 
    if count == 20:
        print ('20 student tamam.')
        break

print("*******************************************************")

print ('khosh amadid')
print ('kafe restoran Anosheh')

while True:
    menu = input('1.cafe 2.fastfood 3.restooran 4.bar 5.board game 6.exit:')
    match menu:
        case '1':
            menu_cafe = input (' 1.late....350  2.cake....200  3. esperso....250  4.cappuccino....300  5.exit:')
            match menu_cafe:
                case '1':
                    num_late = int(input( ' num of order:'))
                    price_late = num_late * 350
                    price_late_txt = price_late * 1.1
                    print ('late ----- 350')
                    print ( price_late_txt) 
                case  '2':
                    num_cake = int(input( ' num of order:'))
                    price_cake = num_cake * 200
                    price_cake_txt = price_cake * 1.1
                    print ('cake ----- 200')
                    print ( price_cake_txt)                  
                case  '3':
                    num_espr = int(input( ' num of order:'))
                    price_espr = num_espr * 250
                    price_espr_txt = price_espr * 1.1
                    print ('espr ----- 250')
                    print ( price_espr_txt)
                case  '4':
                    num_capoo = int(input( ' num of order:'))
                    price_capoo = num_capoo * 300
                    price_capoo_txt = price_capoo * 1.1
                    print ('capoo ----- 300')
                    print ( price_capoo_txt) 
                case _ :
                      break
                      
        case '2':
            menu_fast = input (' 1.pizza....500  2.bueger....350  3. hotdog....250  4.fries....150  5.exit:')
            match menu_fast:
                case '1':
                    num_pizza = int(input( ' num of order:'))
                    price_pizza = num_pizza * 500
                    price_pizza_txt = price_pizza * 1.1
                    print ('pizza ----- 500')
                    print ( price_pizza_txt) 
                case  '2':
                    num_burgr = int(input( ' num of order:'))
                    price_burgrr = num_burgr * 350
                    price_burgr_txt = price_burgr * 1.1
                    print ('burgr ----- 350')
                    print ( price_burgr_txt)                  
                case  '3':
                    num_hot = int(input( ' num of order:'))
                    price_hot = num_hot * 250
                    price_hot_txt = price_hot * 1.1
                    print ('hot ----- 250')
                    print ( price_hot_txt)
                case  '4':
                    num_fries = int(input( ' num of order:'))
                    price_fries = num_fries * 150
                    price_fries_txt = price_fries * 1.1
                    print ('fries ----- 150')
                    print ( price_fries_txt) 
                case _ :
                    break    

        case '3':
            menu_res = input (' 1.koobide....450  2.joojeh....400  3. ghorme....380  4.zereshkpolo....150  5.exit:')
            match menu_res:
                case '1':
                    num_koo = int(input( ' num of order:'))
                    price_koo = num_koo * 450
                    price_koo_txt = price_koo * 1.1
                    print ('koo ----- 450')
                    print ( price_koo_txt) 
                case  '2':
                    num_jooj = int(input( ' num of order:'))
                    price_jooj = num_jooj * 400
                    price_jooj_txt = price_jooj * 1.1
                    print ('jooj ----- 400')
                    print ( price_jooj_txt)                  
                case  '3':
                    num_ghor = int(input( ' num of order:'))
                    price_ghor = num_ghor * 380
                    price_ghor_txt = price_ghor * 1.1
                    print ('ghor ----- 380')
                    print ( price_ghor_txt)
                case  '4':
                    num_zere = int(input( ' num of order:'))
                    price_zere = num_zere * 150
                    price_zere_txt = price_zere * 1.1
                    print ('zere ----- 150')
                    print ( price_zere_txt) 
                case _ :
                    break 

        case '4':
                    menu_bar = input (' 1.mohito....280  2.lemonad....200  3. bluehawaii....320  4.smoothie....300  5.exit:')
                    match menu_bar:
                        case '1':
                            num_mohi = int(input( ' num of order:'))
                            price_mohi = num_mohi * 280
                            price_mohi_txt = price_mohi * 1.1
                            print ('mohi ----- 280')
                            print ( price_mohi_txt) 
                        case  '2':
                            num_lemo = int(input( ' num of order:'))
                            price_lemo = num_lemo * 200
                            price_lemo_txt = price_lemo * 1.1
                            print ('lemo ----- 200')
                            print ( price_lemo_txt)                  
                        case  '3':
                            num_blue = int(input( ' num of order:'))
                            price_blue = num_blue * 320
                            price_blue_txt = price_blue * 1.1
                            print ('blue ----- 320')
                            print ( price_blue_txt)
                        case  '4':
                            num_smoo = int(input( ' num of order:'))
                            price_smoo = num_smoo * 300
                            price_smoo_txt = price_smoo * 1.1
                            print ('smoo ----- 300')
                            print ( price_smoo_txt) 
                        case _ :
                            break                                         

        case '5':
                            menu_game = input (' 1.mafia....280  2.pantomim....350  3. shatranj....400  4.dooz....150  5.exit:')
                            match menu_game:
                                case '1':
                                    num_mafi = int(input( ' num game:'))
                                    price_mafi = num_mafi * 280
                                    price_mafi_txt = price_mafi * 1.1
                                    print ('mafi ----- 280')
                                    print ( price_mafi_txt) 
                                case  '2':
                                    num_panto = int(input( ' num game:'))
                                    price_panto = num_panto * 350
                                    price_panto_txt = price_panto * 1.1
                                    print ('panto ----- 350')
                                    print ( price_panto_txt)                  
                                case  '3':
                                    num_shat = int(input( ' num of game:'))
                                    price_shat = num_shat * 400
                                    price_shat_txt = price_shat * 1.1
                                    print ('shat ----- 400')
                                    print ( price_shat_txt)
                                case  '4':
                                    num_dooz = int(input( ' num of game:'))
                                    price_dooz = num_dooz * 150
                                    price_dooz_txt = price_dooz * 1.1
                                    print ('dooz ----- 150')
                                    print ( price_dooz_txt) 
                                case _ :
                                    break 
        case '6':
            print ( ' khodahafez' )
            break                                                                 

        
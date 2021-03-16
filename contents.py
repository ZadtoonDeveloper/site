import os
words = '''аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон
выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова
кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка
медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень
орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон
тюлень утка форель хорек черепаха ястреб ящерица'''.split()
words_ = {"животные":'''аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон
выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова
кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка
медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень
орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон
тюлень утка форель хорек черепаха ястреб ящерица'''.split(), "спорт":"""бейсбол футбол теннис гольф кросовки мяч 
матч гол""".split(), "транспорт":"""мотоцыкл авто скутер лодка автобус тролейбус трамвай метро поезд самолёт
 велосипед""".split(), "технологии":"""компьютер смартфон интернет роутер ноутбук программа
  ракета чип криптовалюта""".split()}
HANGMAN_PICS = ['''
+---+
    |
    |
    |
  ===
''',
'''
+---+ 
0   |
    |
    |
  ===
''',
'''
 +---+
 0   |
 |   |
     |
   ===
''',
'''
 +---+
 0   |
/|   |
     |
   ===
''',
'''
 +---+
 0   |
/|\  |
     |
   ===
''',
'''
 +---+
 0   |
/|\  |
/    |
   ===
''',
'''
 +---+
 0   |
/|\  |
/ \  |
   ===
 ''']



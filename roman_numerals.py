num_romani =[( 'M',  1000 ), ( 'CM',  900 ),( 'D',   500 ), ( 'CD',  400 ),( 'C',   100 ),( 'XC',   90 ),( 'L',    50 ), ( 'XL',   40 ), ( 'X',    10 ), ( 'IX',    9 ),( 'V',     5 ), ( 'IV',    4 ),( 'I',     1 )]

def converter(num):
    ris = ""
    for num, x in num_romani:
         while num >= x:
            ris += num
            num -= x
    return ris

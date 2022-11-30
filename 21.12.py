def minrotatii(cod_p, cod_adevarat):
 
    rotatii = 0;
 
    
    while (cod_p > 0 or cod_adevarat > 0):
 
        
        input_digit = cod_p % 10;
        code_digit = cod_adevarat % 10;
 
        
        rotatii += min(abs(input_digit - code_digit),
                    10 - abs(input_digit - code_digit));
 
        
        cod_p = int(cod_p / 10);
        cod_adevarat = int(cod_adevarat / 10);
 
    return rotatii;
 

cod_p =int(input('Introdu codul presupus='))
cod_adevarat = 5789;
print("Minimum Rotation =",
       minrotatii(cod_p, cod_adevarat))

def atoi_bussiness(self, string):
    ascii_number_of_0 = ord('0')
    ascii_number_of_9 = ord('9')
    ascii_number_of_negetive = ord('-')
    ascii_number_of_positive = ord('+')
    flag = False
    res = 0
    
    
    for i in range(len(string)):
        
        temp_ord = ord(string[i])
        
        if string[i] == ' ':
            continue
        if temp_ord < ascii_number_of_0 or temp_ord > ascii_number_of_9:
            if temp_ord != ascii_number_of_negetive and temp_ord != ascii_number_of_positive:
                break
            
                
           
        if string[i] == '-' and res == 0:
            flag = True
            continue
        
        temp_num = temp_ord - ascii_number_of_0
        
        if temp_num >= 0 and temp_num < 10:
            if res == 0 and temp_num == 0:
                continue
            res = res * 10 + temp_num
        else :
            if string[i] != '+':
                break
        
        
    return res if flag == False else (-1 * res)
class AtoiInteractor:
    def __init__(self) -> None:
        pass

    def set_params(self, data):
        self.atoi_string = data['atoi_string']
        self.ascii_number_of_0 = ord('0')
        self.ascii_number_of_9 = ord('9')
        self.ascii_number_of_negetive = ord('-')
        self.ascii_number_of_positive = ord('+')
        self.flag = False
        self.res = 0
    
    def __atoi_bussiness(self):
        for i in range(len(self.atoi_string)):
            
            temp_ord = ord(self.atoi_string[i])
            
            if self.atoi_string[i] == ' ':
                continue
            if temp_ord < self.ascii_number_of_0 or temp_ord > self.ascii_number_of_9:
                if temp_ord != self.ascii_number_of_negetive and temp_ord != self.ascii_number_of_positive:
                    break
                
            if self.atoi_string[i] == '-' and self.res == 0:
                self.flag = True
                continue
            
            temp_num = temp_ord - self.ascii_number_of_0
            
            if temp_num >= 0 and temp_num < 10:
                if self.res == 0 and temp_num == 0:
                    continue
                self.res = self.res * 10 + temp_num
            else :
                if self.atoi_string[i] != '+':
                    break
            
        return self.res if self.flag == False else (-1 * self.res)

    def excute(self):
        return self.__atoi_bussiness()

   

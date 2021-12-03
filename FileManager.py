class FileManager:
    
    def __init__(self, dbm):
        self.dbm = dbm
        pass
    
    
    def load_csv(self, file):
        
        with open(file, mode='r') as infile:
            
            line_num = 0
            
            for line in infile:
                
                if(line_num == 0):
                    keys = line.strip().split(',')
                    print(keys)
                else:
                    vals = line.strip().split(',')
                    
                    car = {}
                    
                    for i in range(len(keys)):
                        car[keys[i]] = vals[i]
                        
                    ID = car['ID']
                    
                    if ID.isnumeric():
                        self.dbm.create_car(
                            car['ID'],
                            car['Make'],
                            car['Model'],
                            car['Year'],
                            car['Body'],
                            )
                
                line_num += 1
                
                # if line_num > 15:
                #     break
            
        pass
    

if __name__ =="__main__":
    fm = FileManager()
    fm.load_csv("cars.csv")
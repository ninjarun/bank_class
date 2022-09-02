import json
class Regular:
    name=''
    id=''
    balance=int(0)
    type=''
    

    def __init__(self,name='',id='',balance=0,type='') -> None:
        self.name=name
        self.id=id
        self.balance=balance
        self.type=type


    def __str__(self) -> str:
       return json.dumps({"name":self.name, "id":self.id,"balance":self.balance,"type":self.type})
        
class Premium(Regular):
    pass
class Vip(Regular):
    pass
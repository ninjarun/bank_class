from genericpath import exists
from textwrap import indent
from BankEnums import BankActions, ClientActions, ClientType, MainMenu
from helper_bank_functions import worker_menu
from helper_client_functions import client_menu
from regular_class import *

def main():
    clients=[]
    data_file='bank.json'
    chk_json(data_file)
    MM_menu(clients)
    save_json(clients,data_file)

def chk_json(data):
    if exists(data):
        pass
    else:
        with open(data,'w')as f:
            x=[]
            json.dump(x,f)

def save_json(client_list,data):
    with open(data,'r+')as f:
        file=json.load(f)

    res=[]
    for client in client_list:
        res.append(json.loads(client.__str__()))
    for i in file:
        res.append(i)
    print(res)
    with open(data,'w')as f:
        json.dump(res,f,indent=4)
        
        # f.seek(0)
        # json.dump(res,f,indent=4)

def MM_menu(clients):
    select=None
    while select != int(0):
        for i in MainMenu:
            print(f' -{i.value} - {i.name}')
        select=int(input('select: '))
        if select==MainMenu.WORKER.value:worker_menu(clients)
        if select==MainMenu.CLIENT.value:client_menu(clients)

if __name__ == "__main__":
    main()
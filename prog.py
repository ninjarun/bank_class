from genericpath import exists
from textwrap import indent
from BankEnums import BankActions, ClientActions, ClientType, MainMenu
from helper_bank_functions import worker_menu
from helper_client_functions import client_menu
from regular_class import *

def main():
    clients=[]
    data_file='bank.json'
    chk_json(clients,data_file)
    MM_menu(clients,data_file)

#check if json file exists - if exists load it into clients list
def chk_json(clients_list,data):
    if exists(data):
        with open(data,'r')as f:
            file=json.load(f)
            for i in file:
                tmp=i['type']
                if tmp== 'Regular':
                    clients_list.append(Regular(i['name'],i['id'],i['balance'],i['type']))
                if tmp=='Premium':
                    clients_list.append(Premium(i['name'],i['id'],i['balance'],i['type']))
                if tmp=='Vip':
                    clients_list.append(Vip(i['name'],i['id'],i['balance'],i['type']))
    else:#else create empty json with list in it
        with open(data,'w')as f:
            x=[]
            json.dump(x,f)

#save main clients list to json file
def save_json(client_list,data):
    with open(data,'r+')as f:
        file=json.load(f)

    res=[]
    for client in client_list:
        res.append(json.loads(client.__str__()))
    
    with open(data,'w')as f:
        json.dump(res,f,indent=4)

def MM_menu(clients,data_file):
    select=None
    while select != int(0):
        save_json(clients,data_file)
        for i in MainMenu:
            print(f' -{i.value} - {i.name}')
        select=int(input('select: '))
        if select==MainMenu.WORKER.value:worker_menu(clients)
        if select==MainMenu.CLIENT.value:client_menu(clients)


if __name__ == "__main__":
    main()
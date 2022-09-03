from BankEnums import *
from regular_class import Premium, Regular, Vip
import json
def worker_menu(clients_list):
    # - MENU - print BankActions Class menu
    for act in BankActions:
        print(f'- {act.value} - {act.name}')
    bnk_select=int(input("select: "))

    # - ADD CLIENT - add client selected
    if bnk_select==BankActions.ADD_ClIENT.value:
       add_client(clients_list)
       return clients_list
        
    # - PRINT -print all selected
    if bnk_select==BankActions.PRINT_ALL.value:
        for client in clients_list:
            x=json.loads(client.__str__())
            tmp_name=x['name']
            tmp_id=x['id']
            tmp_balance=x['balance']
            tmp_type=x['type']

            print('Name:',tmp_name,'ID:',tmp_id,'Balanc: ',tmp_balance,'Type:',tmp_type)

            # print(client.name,client.balance)

    if bnk_select==BankActions.CONFETY_CLIENT.value:pass
             
def add_client(clients_list):
    #print client type menu
    for type in ClientType:
        print(f'- {type.value} - {type.name}')
    type_select=int(input('select: '))
    fname=input('enter clients name: ')
    id=input('enter clients id: ')

    #test if id already exists
    for client in clients_list:
        x=json.loads(client.__str__())
        if id==(x['id']):
            print('id already exists!')
            return
    if type_select==ClientType.REGULAR.value:
        clients_list.append(Regular(fname,id,0,'Regular'))
    if type_select==ClientType.PREMIUM.value:
        clients_list.append(Premium(fname,id,0,'Premium'))
    if type_select==ClientType.VIP.value:
        clients_list.append(Vip(fname,id,0,'Vip'))
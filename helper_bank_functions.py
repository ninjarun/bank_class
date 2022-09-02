from BankEnums import *
from regular_class import Premium, Regular, Vip

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
            print(type(x))
            # print(client.name,client.balance)

    if bnk_select==BankActions.CONFETY_CLIENT.value:pass
             
def add_client(clients_list):
    #print client type menu
    for type in ClientType:
        print(f'- {type.value} - {type.name}')
    type_select=int(input('select: '))
    #tests to define client type
    if type_select==ClientType.REGULAR.value:
        clients_list.append(Regular(input('enter clients name: '),input('enter clients id: '),0,'Regular'))
    if type_select==ClientType.PREMIUM.value:
        clients_list.append(Premium(input('enter clients name: '),input('enter clients id: '),500,'Premium'))
    if type_select==ClientType.VIP.value:
        clients_list.append(Vip(input('enter clients name: '),input('enter clients id: '),1000,'Vip'))
from BankEnums import *
from regular_class import *
def client_menu(clients_list):
    for act in ClientActions:
        print(f'- {act.value} - {act.name}')
    client_select=int(input('select: '))
    if client_select==ClientActions.DEPOSIT.value:ClientDeposite(clients_list)
    if client_select==ClientActions.WITHDRAW.value:Withdraw(clients_list)
    if client_select==ClientActions.GET_BALANCE.value:GetBalance(clients_list)
    # if client_select==ClientActions.GO_BACK.value:MM_menu(clients_list)

def ClientDeposite(clients_list):
    chk_id=input('to what id would you like to deposite? ')
    amount=int((input('how much are you depositing? ')))
    for client in clients_list:
        if client.id == chk_id:
            client.balance+=amount

def Withdraw(clients_list):
    chk_id=input('from what id would you like to withdraw from? ')
    amount=int(input('how much would you like to withdraw?'))
    for client in clients_list:
        if chk_id==client.id:
            if client.balance-amount > 0 and client.type=='Regular':
                client.balance-=amount
            elif client.balance-amount > -2000 and client.type=='Premium':
                client.balance-=amount
            elif client.balance-amount > -2500 and client.type=='Vip':
                client.balance-=amount
            else:print('no money buddy!')
            print(client.balance)
    
def GetBalance(clients_list):
    chk_id=input('what id do you want details for? ')
    for client in clients_list:
        if client.id==chk_id:
            print('Your Balance is: ',client.balance)
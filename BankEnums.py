from enum import Enum

class ClientType(Enum):
    REGULAR =1
    PREMIUM =2
    VIP =3
    
class ClientActions(Enum):
    DEPOSIT =1
    WITHDRAW =2
    GET_BALANCE =3

class BankActions(Enum):
    ADD_ClIENT=1
    PRINT_ALL=2
    CONFETY_CLIENT=3

class MainMenu(Enum):
    WORKER=1
    CLIENT=2
    EXIT=0
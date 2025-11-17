class account:
    def __init__(self,name,acctype,balance):
        self.name=name
        self.acctype=acctype
        self.__balance=balance#private variable

ACC=account("jiya patel","saving",10000)
print(ACC.name)
print(ACC.balance)
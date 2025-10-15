terrorist_organizations = ["LET", "JEM", "HM", "IM", "United Liberation Front of Asom", "National Democratic Front of Bodoland", "People’s Liberation Army", "Communist Party of India (Maoist)"]

#create class 
class BannedWordsException(Exception):
    pass 
while True:
    try:
        domain = input("Enter domain name you want to book")
        if domain in terrorist_organizations:
            raise BannedWordsException
        else:
            print(f"you can book this {domain}")
            break
    except BannedWordsException:
        print("this domain name is not available to book, try other name")


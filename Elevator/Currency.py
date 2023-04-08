import requests
class CurrencyConvertor:

    URL= "https://api.exchangeratesapi.io/latest"
    s1=input("Enter Primary Currency :")
    s2=input("Enter Secondary Currency :")
    # sf=s1+","+s2
    sf=s1
    PARAMS={'base':sf}
    r = requests.get(url = URL, params = PARAMS)
    data=r.json()
    # print(data)
    C1=data['rates'][s1]
    C2=data['rates'][s2]
    print(str(C1)+" "+s1+" ---------> "+str(round(C2,3))+" "+s2)

if __name__=='__main__':
    CurrencyConvertor()
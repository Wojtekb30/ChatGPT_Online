from yahoo_search import search

#Query - zapytanie, string.
#maks - maksymalna liczba adresów.
#zwraca listę składającą się z adresu URL, tytułu strony i fragmentu strony.
def WyszukajNaYahoo(query: str, maks=3):
    lista = []
    if not query:
        return lista
    result = search(query)
    n=0
    for r in result.pages:
        if n>=maks:
            break
        lista.append(str(r.link))
        lista.append(str(r.title))
        lista.append(str(r.text))
        n=n+1
    return lista
def convertitore(secondi, tipo):
    return round(secondi / (tipo * 365.25* 24 * 60 * 60), 2)

def terra(secondi):
    return convertitore(secondi, 1)
def mercurio(secondi):
    return convertitore(secondi, 0.2408467)
def venere(secondi):
    return convertitore(secondi, 0.61519726)
def marte(secondi):
    return convertitore(secondi, 1.8808158)
def giove(secondi):
    return convertitore(secondi, 11.862615)
def saturno(secondi):
    return convertitore(secondi, 29.447498)
def urano(secondi):
    return convertitore(secondi, 84.016846)
def nettuno(secondi):
    return convertitore(secondi, 164.79132)
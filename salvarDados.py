
import requests
import pandas as pd
import time
import os

# API base
BASE = "https://api.worldbank.org/v2/pais/{pais}/indicador/{indicador}?format=json"


indicadores = {
    "population": "SP.POP.TOTL",
    "gdp_per_capita": "NY.GDP.PCAP.CD",
    "labour_force": "SL.TLF.TOTL.IN",
    "employment_agriculture_pct": "SL.AGR.EMPL.ZS",
    "female_labour_participation": "SL.TLF.CACT.FE.NE.ZS"
}

paises = [
    "US","CN","IN","BR","RU","DE","GB","FR","JP","CA",
    "AU","ZA","MX","ID","TR","SA","EG","NG","AR","ES"
]

def buscar_indicador(pais, indicador):
    url = BASE.format(pais=pais, indicador=indicador)
    r = requests.get(url)
    if r.status_code != 200:
        return None
    data = r.json()
    if not data or len(data)<2:
        return None
    
    for entry in data[1]:
        if entry['value'] is not None:
            return entry['value']
    return None

def main():
    rows = []
    for c in paises:
        row = {"pais": c}
        for col, ind in indicadores.items():
            val = buscar_indicador(c, ind)
            row[col] = val
            time.sleep(0.2)  
        rows.append(row)

    df = pd.DataFrame(rows)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/paises_data.csv", index=False)

    for col in df.columns:
        if col != "pais":
            df[["pais", col]].to_csv(f"data/{col}.csv", index=False)

    print("Dados obtidos e salvos em data")

if __name__ == "__main__":
    main()

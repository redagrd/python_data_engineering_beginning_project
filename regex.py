# valider les noms avec regex
# valider les email en regex
# tansformer les dates us en dates fr
import pandas as pd
import re
from datetime import datetime

data = pd.read_csv("clients.csv")

data["birthdate"] = pd.to_datetime(data["birthdate"], format="%m-%d-%Y")
data["birthdate"] = data["birthdate"].dt.strftime("%d-%m-%Y")
# print(data.head)

regex_name = r"^[A-Za-z- ]+$"
regex_email = r"^[A-Za-z0-9]+[-_.]?[A-Za-z0-9]+@[A-Za-z0-9]+[-_.]?[A-Za-z0-9]+\.[A-Za-z]{2,3}$"


data_valide = data["firstname"].str.match(
    regex_name) + data["lastname"].str.match(regex_name) + data["email"].str.match(regex_email)
print(data_valide.head())

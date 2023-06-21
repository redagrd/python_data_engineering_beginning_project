import pandas as pd
import matplotlib.pyplot as plt
file_path = "clients.csv"
data = pd.read_csv(file_path)
#print(data.head())

#data.info()
professions = data['profession'].value_counts()
#print(professions)
countries = data['country'].value_counts()
#print(countries)

people_d = data[data['lastname'].str.startswith('D')].head(10)
#print(people_d)

contact_info = data[['firstname', 'lastname', 'email']]
#print(contact_info)

sorted_data = data.sort_values(by=['lastname'])
#print(sorted_data)

#sorted_data.to_csv('sorted_data.csv', index=False)
most_common_city = data['city'].mode().iloc[0]
#print("La ville la plus fréquente est :", most_common_city)

data_scientists = data[data["profession"] == "data scientist"]
#print(data_scientists)

data["birthdate"] = pd.to_datetime(data["birthdate"], format = "%m-%d-%Y")

def calcule_age(birthdate):
    today = birthdate.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

data["age"] = data["birthdate"].apply(calcule_age)
#print(data["age"])
age_par_profession = data.groupby("profession")['age'].mean()
#print(age_par_profession)

average_salary_by_profession = data.groupby("profession")["salary"].mean()
#print(average_salary_by_profession)

big_salary = data[data["salary"] > 5000]
#print(big_salary)

percent_by_country = data["country"].value_counts(normalize=True) * 100
#print(percent_by_country)

max_salary_by_country = data.groupby("country")["salary"].max()
min_salary_by_country = data.groupby("country")["salary"].min()
#print("Salaire maximum par pays :\n", max_salary_by_country)
#print("Salaire minimum par pays :\n",min_salary_by_country)

def calculate_age(birthdate):
    today = birthdate.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
data["age"] = data["birthdate"].apply(calcule_age)
age_30 = data[data["age"] == 30]
#print(age_30)

age_bins = [0,10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
age_labels = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89","90-100"]
data["age_group"] = pd.cut(data["age"], bins=age_bins, labels=age_labels, include_lowest=True)
people_by_age_group = data["age_group"].value_counts()
#print(people_by_age_group)

salary_bins = range(0,int(data["salary"].max()),10) # 0 à 1000 par pas de 10
plt.hist(data["salary"], bins=salary_bins, edgecolor="green") #bins pour les intervalles de salaire
plt.title("Répartition des salaires")
plt.xlabel("Salaire")
plt.ylabel("Nombre de personnes")
plt.show()

same_family_name = data[data["lastname"].duplicated(keep=False)].sort_values(by="lastname") #duplicated pour trouver les doublons et keep=False pour garder les doublons, sort_values pour trier par nom de famille croissant 
#print(same_family_name)

profession_by_country = data.groupby(["country","profession"]).size().unstack()
"""
    .size(): Cette méthode calcule le nombre de professionnels dans chaque groupe créé par le regroupement précédent. 
    Le résultat est une série pandas contenant le nombre de professionnels pour chaque combinaison pays/profession.
    .unstack(): Cette méthode transforme la série de résultats en un tableau croisé, où chaque colonne représente une profession et chaque ligne représente un pays. 
    Les valeurs dans le tableau sont le nombre de professionnels pour chaque combinaison pays/profession. 
    Si une combinaison n'a pas de valeur, elle sera remplie par NaN (Not a Number).
"""
print(profession_by_country)

#valider les noms avec reges
#valider les email en regex
#tansformer les dates us en dates fr
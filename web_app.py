import pandas as pd
import streamlit as st
import joblib

model = joblib.load('XGBosstModel.joblib')

addres = [
    "Abazar", "Abbasabad", "Abuzar", "Afsarieh", "Ahang", "Air force", "Ajudaniye", "Alborz Complex",
    "Aliabad South", "Amir Bahador", "Amirabad", "Amirieh", "Andisheh", "Aqdasieh", "Araj", "Atabak", "Azadshahr", "Azarbaijan", "Azari",
    "Baghestan", "Bahar", "Baqershahr", "Beryanak", "Boloorsazi", "Central Janatabad", "Chahardangeh", "Chardangeh", "Chardivari", "Chidz",
    "Damavand", "Darabad", "Darakeh", "Darband", "Daryan No", "Dehkade Olampic", "Dezashib", "Dolatabad", "Dorous", "East Ferdows Boulevard",
    "East Pars", "Ekbatan", "Ekhtiarieh", "Elahieh", "Elm-o-Sanat", "Enghelab", "Eram", "Eskandari", "Fallah", "Farmanieh", "Fatemi",
    "Feiz Garden", "Firoozkooh", "Firoozkooh Kuhsar", "Garden of Saba", "Gheitarieh", "Ghiyamdasht", "Ghoba", "Gholhak", "Gisha", "Golestan",
    "Haft Tir", "Hakimiyeh", "Hashemi", "Hassan Abad", "Hekmat", "Heravi", "Heshmatieh", "Hor Square", "Islamshahr", "Islamshahr Elahieh",
    "Javadiyeh", "Jeyhoon", "Jordan", "Kahrizak", "Kamranieh", "Karimkhan", "Karoon", "Kazemabad", "Keshavarz Boulevard", "Khademabad Garden",
    "Khavaran", "Komeil", "Koohsar", "Kook", "Lavizan", "Mahallati", "Mahmoudieh", "Majidieh", "Malard", "Marzdaran", "Mehrabad", "Mehrabad River River",
    "Mehran", "Mirdamad", "Mirza Shirazi", "Moniriyeh", "Narmak", "Nasim Shahr", "Nawab", "Naziabad", "Nezamabad", "Niavaran", "North Program Organization",
    "Northern Chitgar", "Northern Janatabad", "Northern Suhrawardi", "Northren Jamalzadeh", "Ostad Moein", "Ozgol", "Pakdasht", "Pakdasht KhatunAbad",
    "Parand", "Parastar", "Pardis", "Pasdaran", "Persian Gulf Martyrs Lake", "Pirouzi", "Pishva", "Punak", "Qalandari", "Qarchak", "Qasr-od-Dasht",
    "Qazvin Imamzadeh Hassan", "Railway", "Ray", "Ray - Montazeri", "Ray - Pilgosh", "Razi", "Republic", "Robat Karim", "Rudhen", "Saadat Abad",
    "SabaShahr", "Sabalan", "Sadeghieh", "Safadasht", "Salehabad", "Salsabil", "Sattarkhan", "Seyed Khandan", "Shadabad", "Shahedshahr", "Shahr-e-Ziba",
    "ShahrAra", "Shahrake Apadana", "Shahrake Azadi", "Shahrake Gharb", "Shahrake Madaen", "Shahrake Qods", "Shahrake Quds", "Shahrake Shahid Bagheri",
    "Shahrakeh Naft", "Shahran", "Shahryar", "Shams Abad", "Shoosh", "Si Metri Ji", "Sohanak", "Southern Chitgar", "Southern Janatabad",
    "Southern Program Organization", "Southern Suhrawardi", "Tajrish", "Tarasht", "Taslihat", "Tehran Now", "Tehransar", "Telecommunication", "Tenant",
    "Thirteen November", "Vahidieh", "Vahidiyeh", "Valiasr", "Vanak", "Velenjak", "Villa", "Water Organization", "Waterfall", "West Ferdows Boulevard",
    "West Pars", "Yaftabad", "Yakhchiabad", "Yousef Abad", "Zafar", "Zaferanieh", "Zargandeh", "Zibadasht"
]


st.title('Estate Price Prediction!')

Area = st.number_input("Area", 25,value=250)
Room = st.selectbox("Room", [0,1,2,3,4,5],index=1)
Parking = st.radio("Choose Parking", [0,1])
Warehouse = st.radio("Choose Warehouse", [0,1])
Elevator = st.radio("Choose Elevator", [0,1])
x = st.selectbox("Addres", addres, index=addres.index('Pardis'))
temp = []
for _ in addres:
    if _ == x:
        temp.append(1)
    else:
        temp.append(0)

name = ['Area',	'Room',	'Parking', 'Warehouse',	'Elevator'] + addres

def predict():
    row = [Area,Room,Parking,Warehouse,Elevator] + temp
    pre = pd.DataFrame([row], columns=name)
    prediction = model.predict(pre)
    formatted_prediction = '{:,.0f}'.format(prediction[0])
    st.write(f'<h2><span style="color:yellow;">Predicted Price: {formatted_prediction}</span></h2>', unsafe_allow_html=True)

trigger = st.button('Predict', on_click=predict)



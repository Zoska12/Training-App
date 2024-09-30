import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Tytuł aplikacji
st.title('Mens/Womens trainings')

# Wybór między chart_data a chart_data2
st.subheader('Wybierz zestaw danych')
dataset_option = st.selectbox(
    'Wybierz zestaw danych do użycia',
    ('M(1)', 'W(1)')
)

# Definiowanie dynamicznej ścieżki na podstawie wyboru
base_path = r'data'
pickle_file = f"{dataset_option}.pkl"
image_file = f"{dataset_option}.JPG"

# Ładowanie danych dynamicznie
data_path = os.path.join(base_path, pickle_file)
image_path = os.path.join(base_path, image_file)

# Wczytywanie pliku pickle z wybranego zestawu
data = pd.read_pickle(data_path)

# Wyświetlenie odpowiedniego zdjęcia
st.subheader('Zdjęcie treningu')
st.image(image_path, caption=f'Zdjęcie dla {dataset_option}', use_column_width=True)

# Dodatkowy interaktywny komponent - tabela filtrowanych danych
st.subheader('Wczytana Tabela')
st.write(data)

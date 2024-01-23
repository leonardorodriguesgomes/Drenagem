import streamlit as st
import pandas as pd
import pydeck as pdk


def Plataforma(p):
    del(p['Fora Plataforma'])
    del(p["Gasto Plataforma"])
    del(p["Gasto Fora Plataforma"])
    del(p['km'])
    return p

def Fora_plataforma(p):
    del(p['Plataforma'])
    del(p["Gasto Plataforma"])
    del(p["Gasto Fora Plataforma"])
    del(p['km'])
    return p

def Gasto_Plataforma(p):
    del(p['Fora Plataforma'])
    del(p['Plataforma'])
    del(p["Gasto Fora Plataforma"])
    del(p['km'])
    return p

def Gasto_Fora_plataforma(p):
    del(p['Fora Plataforma'])
    del(p['Plataforma'])
    del(p["Gasto Plataforma"])
    del(p['km'])
    return p




def principal():
       
    chart_data = filtrado
    

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=-23.50798,
            longitude=-46.55123,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
               'HeatmapLayer',
               data=chart_data,
               get_position='[LON, LAT]',
               radius=200,
               elevation_scale=0,
               elevation_range=[0,2],
               pickable=True,
               extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[LON, LAT]',
                get_color='[200, 30, 0, 160]',
                get_radius=1,
            ),
        ],))
 


DATA_URL = 'Infodrenagem.xlsx'
arq = pd.read_excel(DATA_URL)


    
option1 = st.sidebar.selectbox(
"Escolha uma opção?",
("Produtividade","Gasto"))

option2 = st.sidebar.selectbox("Escolha um serviço",("Limpeza de drenagem de Plataforma","Limpeza de drenagem Fora de Plataforma"))

if (option1 == "Produtividade"):
    values = st.sidebar.slider(
    'Selecionar um intervalo de produtividade(km/h)',
    0.000, 2.000, (0.000, 2.000))
elif (option1 == "Gasto"):
    values = st.sidebar.slider(
    'Selecionar um intervalo de gasto(R$)',
    0.00, 2000.00, (0.00, 2000.00))


if ((option1 == "Produtividade") and (option2 == "Limpeza de drenagem de Plataforma")):
    option = "Plataforma"
elif ((option1 == "Produtividade") and (option2 == "Limpeza de drenagem Fora de Plataforma")):
    option = "Fora Plataforma"
elif ((option1 == "Gasto") and (option2 == "Limpeza de drenagem de Plataforma")):
    option = "Gasto Plataforma"
elif ((option1 == "Gasto") and (option2 == "Limpeza de drenagem Fora de Plataforma")):
    option = "Gasto Fora Plataforma"


if ((option1 == "Produtividade") and (option2 == "Limpeza de drenagem de Plataforma")):
    arq = Plataforma(arq)
elif ((option1 == "Produtividade") and (option2 == "Limpeza de drenagem Fora de Plataforma")):
    arq = Fora_plataforma(arq)
elif ((option1 == "Gasto") and (option2 == "Limpeza de drenagem de Plataforma")):
    arq = Gasto_Plataforma(arq)
elif ((option1 == "Gasto") and (option2 == "Limpeza de drenagem Fora de Plataforma")):
    arq = Gasto_Fora_plataforma(arq)
    
st.write(option)
#if (option == 'Plataforma'):
#    arq = Plataforma(arq)
#elif (option == 'Fora_Plataforma'):
#    arq = Fora_plataforma(arq)
#elif (option == 'Gasto_plataforma'):
#    arq = Gasto_Plataforma(arq)
#elif (option == 'Gasto_Fora_Plataforma'):
#    arq = Gasto_Fora_plataforma(arq)

 

filtrado1 = arq[arq[str(option)]>=values[0]]
filtrado2 = filtrado1[filtrado1[str(option)]<=values[1]]
filtrado = filtrado2


#st.sidebar.button("Reset", type="primary")
if st.sidebar.button('Iniciar'):
   principal()
   st.write(filtrado)




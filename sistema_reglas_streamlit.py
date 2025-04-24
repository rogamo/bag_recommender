import streamlit as st

# decisiones
recommendation_map = {
    "lujo": {
        "alto": {
            "negro": {
                "chico": "Dior Mini Saddle"
            },
            "blanco": {
                "mediano": "Chanel Classic Handbag"
            },
            "café": {
                "mediano/grande": "Miu Miu Adventure"
            }
        }
    },
    "intermedio": {
        "medio": {
            "negro": {
                "chico": "Bolso Longchamp Negro"
            },
            "blanco": {
                "mediano": "Bolso Guess Blanco"
            },
            "café": {
                "mediano/grande": "Bolso Coach Café"
            }
        }
    },
    "masivo": {
        "bajo": {
            "negro": {
                "chico": "Bolsa Económica Negra"
            },
            "blanco": {
                "mediano": "Bolsa Básica Blanca"
            },
            "café": {
                "mediano/grande": "Bolsa Multiusos Café"
            }
        }
    }
}


def recomendar_bolsa(marca, precio, color, tamaño):
    try:
        return recommendation_map[marca][precio][color][tamaño]
    except KeyError:
        return "error:" \
        " Combinación no válida. Intenta otra."

# Interfaz Streamlit
st.title("Recomendador de Bolsas de Mano")

st.markdown("Elige tus preferencias para recibir una recomendación personalizada:")

# Menús interactivos
marca = st.selectbox("Marca", ["lujo", "intermedio", "masivo"])
precio = st.selectbox("Precio", ["alto", "medio", "bajo"])
color = st.selectbox("Color", ["negro", "blanco", "café"])
tamaño = st.selectbox("Tamaño", ["chico", "mediano", "mediano/grande"])

# Botón para recomendar
if st.button("Obtener recomendación"):
    resultado = recomendar_bolsa(marca, precio, color, tamaño)
    st.success(f"Recomendación: {resultado}")

#python -m streamlit run sistema_reglas_streamlit.py
# install library -  python -m pip install streamlit

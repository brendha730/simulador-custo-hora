
import streamlit as st
from PIL import Image

# Configuração da página
st.set_page_config(layout="wide", page_title="Simulador de Custo Hora", page_icon="🕒")

# Cabeçalho com logo
col1, col2 = st.columns([6, 1])
with col1:
    st.title("Simulador de Custo Hora da Máquina")
    st.markdown("### Preencha os dados abaixo para calcular o custo hora produtivo e improdutivo")
with col2:
    logo = Image.open("logo_direita.png.jpg")  # Altere o caminho se necessário
    st.image(logo, width=80)

# Seção de entrada de dados
st.markdown("## Parâmetros da Máquina")

col_a, col_b = st.columns(2)
with col_a:
    valor_maquina = st.number_input("Valor de aquisição da máquina (R$)", min_value=0.0, step=100.0)
    vida_util_anos = st.number_input("Vida útil estimada (anos)", min_value=1, step=1)
    horas_ano = st.number_input("Horas trabalhadas por ano", min_value=1, step=100)
    manutencao_anual = st.number_input("Custo anual com manutenção (R$)", min_value=0.0, step=100.0)
with col_b:
    energia_mensal = st.number_input("Custo mensal com energia (R$)", min_value=0.0, step=50.0)
    operador_salario = st.number_input("Salário mensal do operador (R$)", min_value=0.0, step=100.0)
    outros_custos = st.number_input("Outros custos mensais (R$)", min_value=0.0, step=100.0)
    produtividade_percent = st.slider("Produtividade (%)", min_value=1, max_value=100, value=85)

# Cálculo
if horas_ano > 0 and vida_util_anos > 0:
    custo_fixo_anual = valor_maquina / vida_util_anos
    custo_variavel_anual = (energia_mensal + operador_salario + outros_custos) * 12 + manutencao_anual
    custo_total_anual = custo_fixo_anual + custo_variavel_anual
    custo_hora_total = custo_total_anual / horas_ano

    # Dividindo custo hora em produtivo e improdutivo
    custo_hora_prod = custo_hora_total * (produtividade_percent / 100)
    custo_hora_improd = custo_hora_total * ((100 - produtividade_percent) / 100)

    st.markdown("## Resultado")
    st.metric("Custo Hora Total", f"R$ {custo_hora_total:.2f}")
    st.metric("Custo Hora Produtivo", f"R$ {custo_hora_prod:.2f}")
    st.metric("Custo Hora Improdutivo", f"R$ {custo_hora_improd:.2f}")

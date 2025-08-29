import gradio as gr
import math

def fatorial(num):
    if num < 0:
        return "Fatorial não definido para números negativos"
    return math.factorial(num)

iface = gr.Interface(
    fn=fatorial,
    inputs="number",
    outputs="number",
    title="Calculadora de fatorial",
    description="Insira o número para obter o número fatorial",
    theme="default"
)

iface.launch()
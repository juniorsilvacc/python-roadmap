import gradio as gr

def reverter(texto):
    reverter_texto = texto[::-1]
    return reverter_texto, len(reverter_texto)

print(reverter("Junior"))

iface = gr.Interface(
    fn=reverter,
    inputs="text",
    outputs=["text", "number"],
    title="Reverter texto",
    description="Insira o texto que você quer reverter",
    theme="default"
)

iface.launch()
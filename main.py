import torch
import gradio as gr
from PyPDF2 import PdfReader
from TTS.api import TTS

# Define o dispositivo correto
device = "cuda" if torch.cuda.is_available() else "cpu"

# Inicializa o modelo de TTS
model_name = "tts_models/multilingual/multi-dataset/your_tts"
tts = TTS(model_name).to(device)

# Verifica se o modelo suporta múltiplos speakers
try:
    available_speakers = tts.speakers if isinstance(tts.speakers, list) else tts.speakers()
    default_speaker = available_speakers[0] if available_speakers else None
except AttributeError:
    available_speakers = None
    default_speaker = None

# Função para converter PDF em MP3
def pdf_to_mp3(pdf_path, speaker=default_speaker, speed=1.0, language="pt-br"):
    reader = PdfReader(pdf_path.name)  # Usa .name para passar o caminho correto

    my_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            my_text += text + " "

    if not my_text.strip():
        return "Erro: Não foi possível extrair texto do PDF."

    out_path = "output.mp3"
    tts.tts_to_file(text=my_text, speaker=speaker, speed=speed, language=language, file_path=out_path)
    
    return out_path

# Interface do Gradio
interface = gr.Interface(
    fn=pdf_to_mp3,
    inputs=[
        gr.File(label="Selecione o PDF"),
        gr.Dropdown(value=default_speaker, choices=available_speakers, label="Voz"),
        gr.Slider(value=1.0, minimum=0.5, maximum=2.0, step=0.1, label="Velocidade"),
        gr.Dropdown(value="pt-br", choices=["en", "es", "fr", "it", "pt-br"], label="Idioma"),
    ],
    outputs=gr.Audio(label="Áudio Gerado"),
    title="Conversor de PDF para MP3",
    description="Converte um arquivo PDF em áudio MP3 usando síntese de voz.",
)

# Inicia a interface
interface.launch()

import streamlit as st
from pytube import YouTube
from io import BytesIO

st.title("Baixar Vídeos/Músicas do YouTube 🎵")

# Input para a URL do YouTube
url = st.text_input("Cole a URL do YouTube aqui:")

if url:
    try:
        yt = YouTube(url)
        st.subheader(yt.title)

        # Escolher entre vídeo ou áudio
        download_type = st.radio("Selecione o tipo de download:", ["Vídeo", "Música"])

        if download_type == "Vídeo":
            # Selecionar a melhor resolução disponível
            stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
        else:
            # Baixar apenas áudio (formato MP4)
            stream = yt.streams.get_audio_only()

        # Baixar para um buffer de memória (sem salvar no servidor)
        buffer = BytesIO()
        stream.stream_to_buffer(buffer)
        buffer.seek(0)

        # Botão de download
        st.download_button(
            label="Clique para baixar" if download_type == "Vídeo" else "Baixar música",
            data=buffer,
            file_name=f"{yt.title}.{stream.subtype}" if download_type == "Vídeo" else f"{yt.title}.mp3",
            mime="video/mp4" if download_type == "Vídeo" else "audio/mp3"
        )

    except Exception as e:
        st.error(f"Erro: {e}")
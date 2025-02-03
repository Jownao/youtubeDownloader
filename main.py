import streamlit as st
from pytubefix import YouTube
from io import BytesIO

# Configuração inicial da página
st.set_page_config(
    page_title="YouTube Downloader",
    page_icon="🎬",
    layout="centered"
)

# Sistema de internacionalização
TEXT = {
    "pt": {
        "title": "🎬 YouTube Downloader",
        "subtitle": "**Baixe vídeos e músicas diretamente do YouTube**",
        "instructions_title": "ℹ️ Instruções",
        "instructions": [
            "1. Cole a URL do vídeo",
            "2. Escolha o tipo de download",
            "3. Clique no botão de download"
        ],
        "warning": "⚠️ **Aviso Legal**  \nSó baixe conteúdo com autorização do autor!",
        "url_label": "**Cole sua URL do YouTube aqui:**",
        "url_placeholder": "Ex: https://youtube.com/watch?v=...",
        "thumbnail": "Thumbnail do Vídeo",
        "channel": "👤 Canal: {}",
        "duration": "⏱ Duração: {}",
        "download_type": "**Selecione o tipo de download:**",
        "video": "🎥 Vídeo",
        "music": "🎧 Música",
        "download_btn": "⬇️ Baixar {}",
        "loading": "Preparando download...",
        "error": "❌ Erro: {}",
        "footer": "Desenvolvido por © Jownao usando Streamlit | pytubefix"
    },
    "en": {
        "title": "🎬 YouTube Downloader",
        "subtitle": "**Download videos and music directly from YouTube**",
        "instructions_title": "ℹ️ Instructions",
        "instructions": [
            "1. Paste the video URL",
            "2. Choose download type",
            "3. Click download button"
        ],
        "warning": "⚠️ **Legal Warning**  \nOnly download authorized content!",
        "url_label": "**Paste your YouTube URL here:**",
        "url_placeholder": "Ex: https://youtube.com/watch?v=...",
        "thumbnail": "Video Thumbnail",
        "channel": "👤 Channel: {}",
        "duration": "⏱ Duration: {}",
        "download_type": "**Select download type:**",
        "video": "🎥 Video",
        "music": "🎧 Music",
        "download_btn": "⬇️ Download {}",
        "loading": "Preparing download...",
        "error": "❌ Error: {}",
        "footer": "Made by © Jownao using Streamlit | pytubefix"
    }
}

# Inicializar estado de linguagem
if 'lang' not in st.session_state:
    st.session_state.lang = 'pt'

# Função para trocar idioma
def toggle_language():
    st.session_state.lang = 'en' if st.session_state.lang == 'pt' else 'pt'

# CSS customizado 
st.markdown("""
<style>
    .header { padding: 1rem 0; text-align: center; }
    .thumbnail { border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
    .download-btn { width: 100%; margin-top: 1rem; }
    .info-box { padding: 1.5rem; background: #f8f9fa; border-radius: 10px; margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)

# Componentes da interface
with st.container():
    st.markdown('<div class="header">', unsafe_allow_html=True)
    st.title(TEXT[st.session_state.lang]['title'])
    st.markdown(TEXT[st.session_state.lang]['subtitle'])
    st.markdown('</div>', unsafe_allow_html=True)

# Barra lateral com seletor de idioma
with st.sidebar:
    # Botão de troca de idioma
    col1, col2 = st.columns([1,3])
    with col1:
        st.button(
            "🇧🇷/🇺🇸" if st.session_state.lang == 'pt' else "🇺🇸/🇧🇷",
            on_click=toggle_language,
            help="Switch language" if st.session_state.lang == 'en' else "Mudar idioma"
        )
    
    st.header(TEXT[st.session_state.lang]['instructions_title'])
    for line in TEXT[st.session_state.lang]['instructions']:
        st.markdown(line)
    st.markdown("---")
    st.markdown(TEXT[st.session_state.lang]['warning'])

# Widget principal
url = st.text_input(
    TEXT[st.session_state.lang]['url_label'],
    placeholder=TEXT[st.session_state.lang]['url_placeholder']
)

if url:
    try:
        yt = YouTube(url)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(
                yt.thumbnail_url,
                caption=TEXT[st.session_state.lang]['thumbnail'],
                use_container_width=True,
                width=250
            )
        
        with col2:
            st.subheader(f"🎵 {yt.title}")
            st.caption(TEXT[st.session_state.lang]['channel'].format(yt.author))
            duration = f"{yt.length // 60}:{yt.length % 60:02}"
            st.caption(TEXT[st.session_state.lang]['duration'].format(duration))
            
            download_type = st.radio(
                TEXT[st.session_state.lang]['download_type'],
                [TEXT[st.session_state.lang]['video'], TEXT[st.session_state.lang]['music']],
                horizontal=True
            )
            
            if TEXT[st.session_state.lang]['video'] in download_type:
                stream = yt.streams.filter(
                    progressive=True,
                    file_extension="mp4"
                ).get_highest_resolution()
                mime_type = "video/mp4"
                file_ext = "mp4"
            else:
                stream = yt.streams.get_audio_only()
                mime_type = "audio/mp3"
                file_ext = "mp3"
            
            buffer = BytesIO()
            
            with st.spinner(TEXT[st.session_state.lang]['loading']):
                stream.stream_to_buffer(buffer)
                buffer.seek(0)
            
            st.download_button(
                label=TEXT[st.session_state.lang]['download_btn'].format(
                    TEXT[st.session_state.lang]['video'].split()[-1] if 'video' in download_type.lower() 
                    else TEXT[st.session_state.lang]['music'].split()[-1]
                ),
                data=buffer.getvalue(),
                file_name=f"{yt.title[:30]}.{file_ext}",
                mime=mime_type,
                use_container_width=True
            )

    except Exception as e:
        st.error(TEXT[st.session_state.lang]['error'].format(str(e)))

# Rodapé
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #666; font-size: 0.9em;">
    {TEXT[st.session_state.lang]['footer']}
</div>
""", unsafe_allow_html=True)
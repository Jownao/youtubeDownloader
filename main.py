import streamlit as st
from pytubefix import YouTube
from io import BytesIO

# Configuração inicial da página
st.set_page_config(
    page_title="YouTube Downloader",
    page_icon="🎬",
    layout="centered"
)

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
    st.title("🎬 YouTube Downloader")
    st.markdown("**Baixe vídeos e músicas diretamente do YouTube**")
    st.markdown('</div>', unsafe_allow_html=True)

# Barra lateral para informações
with st.sidebar:
    st.header("ℹ️ Instruções")
    st.markdown("""
    1. Cole a URL do vídeo
    2. Escolha o tipo de download
    3. Clique no botão de download
    """)
    st.markdown("---")
    st.markdown("⚠️ **Aviso Legal**  \nSó baixe conteúdo com autorização do autor!")

# Widget principal
url = st.text_input(
    "**Cole sua URL do YouTube aqui:**",
    placeholder="Ex: https://youtube.com/watch?v=..."
)

if url:
    try:
        yt = YouTube(url)
        
        # Layout em colunas para thumbnail e informações
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image(
                yt.thumbnail_url,
                caption="Thumbnail do Vídeo",
                use_container_width=True,  # Corrigido aqui
                width=250
            )
        
        with col2:
            st.subheader(f"🎵 {yt.title}")
            st.caption(f"👤 Canal: {yt.author}")
            st.caption(f"⏱ Duração: {yt.length // 60}:{yt.length % 60:02}")
            
            download_type = st.radio(
                "**Selecione o tipo de download:**",
                ["🎥 Vídeo", "🎧 Música"],
                horizontal=True
            )
            
            # Configurações de download
            if "Vídeo" in download_type:
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
            
            # Corrigindo o buffer
            buffer = BytesIO()
            
            with st.spinner("Preparando download..."):
                stream.stream_to_buffer(buffer)  
                buffer.seek(0)
            
            # Botão de download estilizado
            st.download_button(
                label=f"⬇️ Baixar {download_type.split()[-1]}",
                data=buffer.getvalue(),  
                file_name=f"{yt.title[:30]}.{file_ext}",
                mime=mime_type,
                use_container_width=True,
                key=f"download_{file_ext}",
                help="Clice para iniciar o download"
            )

    except Exception as e:
        st.error(f"❌ Erro: {str(e)}")

# Rodapé
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em;">
    Desenvolvido por © Jownao usando Streamlit | pytubefix
</div>
""", unsafe_allow_html=True)
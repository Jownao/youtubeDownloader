
# 📥 YouTube Downloader

Aplicativo web para baixar vídeos e músicas do YouTube de forma simples e rápida, com interface minimalista.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://jownaoytdownloader.streamlit.app/)

## ✨ Funcionalidades

- **Download de vídeos** na melhor resolução disponível
- **Extração de áudio** em formato MP3
- Visualização da thumbnail do vídeo
- Informações detalhadas (título, canal, duração)


## 🚀 Como usar

### Pré-requisitos
- Python 3.8+
- pip

### Instalação
```bash
# Clonar repositório
git clone https://github.com/seu-usuario/youtube-downloader.git

# Acessar diretório
cd youtube-downloader

# Instalar dependências
pip install -r requirements.txt
```

### Executando a aplicação
```bash
streamlit run app.py
```

## ⚙️ Tecnologias
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [pytubefix](https://github.com/DeltaR115/pytubefix)

## 📋 Arquitetura
```plaintext
.
├── main.py           # Código principal
├── requirements.txt  # Dependências
└── README.md         # Documentação

```

## ⚠️ Considerações Legais
Este projeto é destinado apenas para fins educacionais. Respeite os direitos autorais e:
- Não baixe conteúdo protegido sem autorização
- Verifique as leis de sua região
- Delete arquivos baixados após testes

## 🛠️ Solução de Problemas Comuns

### Erro 403 Forbidden
```bash
# Atualize o pytubefix
pip install --upgrade git+https://github.com/DeltaR115/pytubefix.git
```

### Download não inicia
- Verifique sua conexão com internet
- Teste com diferentes URLs
- Reinicie a aplicação


---

**Nota:** Este projeto não tem relação com o YouTube/Google. Use com responsabilidade.




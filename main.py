import os
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.chains.summarize import load_summarize_chain
from langchain.schema import Document
import streamlit as st
import tempfile

# Config
os.environ['OPENAI_API_KEY'] = 'votre-cle-api'  # Ou via .env
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
chain = load_summarize_chain(llm, chain_type="map_reduce")

def extract_text(pdf_file):
    """Extrait le texte d'un PDF."""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def summarize_pdf(pdf_file):
    """Summarise via map-reduce."""
    text = extract_text(pdf_file)
    chunks = text_splitter.split_text(text)
    docs = [Document(page_content=chunk) for chunk in chunks]
    summary = chain.invoke(docs)
    return summary['output_text']

# Interface Streamlit
st.title("🧠 AI PDF Summarizer")
uploaded_file = st.file_uploader("Choisissez un PDF", type="pdf")
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name
    if st.button("Summariser"):
        with st.spinner("Analyse en cours..."):
            summary = summarize_pdf(open(tmp_path, 'rb'))
        st.success("Résumé généré !")
        st.markdown(summary)
        st.download_button("Télécharger TXT", summary, "resume.pdf.txt")

# AI PDF Summarizer - Résumés intelligents de documents académiques



**Summarizeur de PDF piloté par IA** utilisant PyMuPDF + LangChain "map-reduce" pour documents volumineux (articles scientifiques, rapports H2, thèses). Résumés concis et structurés en 1 clic via interface Streamlit.

## Fonctionnalités
- Extraction texte optimisée (PyMuPDF)
- Chunking intelligent (2000 tokens/chemin avec overlap)
- Summarisation "map-reduce" GPT-4o-mini (gère 100+ pages)
- Interface web Streamlit avec téléchargement TXT
- Variante offline Ollama (Llama3) incluse

## Installation
```bash
git clone https://github.com/salimklibi/pdf_summarizer.git
cd ai-pdf-summarizer
conda create -n pdf-ai python=3.10
conda activate pdf-ai
pip install -r requirements.txt
```

**requirements.txt** :
```
pymupdf==1.24.9
langchain==0.2.16
langchain-openai==0.1.14
tiktoken==0.6.0
streamlit==1.35.0
python-dotenv
# Offline: pip install langchain-community ollama
```

## Configuration API
```bash
# OpenAI (recommandé)
echo "OPENAI_API_KEY=sk-..." > .env

# OU Offline Ollama
ollama pull llama3
```

## Utilisation
```bash
streamlit run summarizer.py
```
1. Uploadez PDF (articles MCDA, rapports hydrogène, thèses)
2. Cliquez **"Summariser"** → Résumé structuré en 30s
3. **Téléchargez TXT** pour notes de littérature review

## Personnalisation
Modifiez le prompt dans `summarizer.py` :
```python
prompt = "Résumez les résultats MCDA, implications territoriales et recommandations H2 pour Pays de la Loire"
```

## Exemple Résumé
**Input** : Rapport 50 pages sur electrolyseurs PEM/AEM  
**Output** : "L'analyse TOPSIS classe PEM > AEM sur coût/infrastructures. Vendée : potentiel ENR 82/100, classée 6e nationale. Recommandation : mix 70% local H2."

## Outputs
- `resume.pdf.txt` : Résumé téléchargeable
- Interface web réactive (mobile/desktop)
- Logs token usage pour monitoring coûts

## Variante Offline
```python
# Remplacez ChatOpenAI par:
from langchain_community.llm import ChatOllama
llm = ChatOllama(model="llama3", temperature=0)
```

## Dépendances Optionnelles
- **Académique** : Ajoutez `pymupdf` pour tableaux/figures
- **Batch** : `pathlib` pour résumer dossiers entiers
- **Export** : `reportlab` pour PDF résumé formaté

## Licence et Contribution
**MIT License**. Parfait pour littérature review PhD hydrogène Paris-Dauphine. PR bienvenues pour prompts spécialisés MCDA/techno-éco.

```
Auteur: Salim KLIBI - PhD Decision analysis & H2 energy Systems
LinkedIn: https://www.linkedin.com/in/salim-klibi/
```

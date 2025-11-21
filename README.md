# Agent IA YouTube

Un projet d'agent IA capable d'analyser et de synthétiser des documents PDF, avec génération de synthèse vocale.

## 🚀 Fonctionnalités

- Analyse de documents PDF
- Extraction et traitement du texte
- Génération de résumés structurés
- Synthèse vocale des résultats
- Interface API REST
- Stockage vectoriel avec Pinecone
- Support multilingue (traduction en français)

## 🛠️ Technologies Utilisées

- FastAPI pour l'API backend
- LlamaIndex pour le traitement de documents
- OpenAI Embeddings pour l'analyse sémantique
- Pinecone pour le stockage vectoriel
- PyMuPDF pour la lecture de PDF
- Speechify pour la synthèse vocale

## ⚙️ Prérequis

- Python 3.8+
- Poetry pour la gestion des dépendances
- Clés API pour :
  - OpenAI
  - Pinecone
  - Langfuse
  - Speechify
  - MistralAI (optionnel)

## 🔧 Installation

1. Cloner le dépôt :
```bash
git clone [URL_DU_REPO]
cd agent-ia-youtube
```

2. Installer les dépendances avec Poetry :
```bash
poetry install
```

3. Configurer les variables d'environnement :
Créer un fichier `.env` à la racine du projet avec les variables suivantes :
```
OPENAI_API_KEY=votre_clé_openai
PINECONE_API_KEY=votre_clé_pinecone
MISTRALAI_API_KEY=votre_clé_mistral
HF_ACCESS_TOKEN=votre_token_huggingface
SPEECHIFY_API_KEY=votre_clé_speechify
LANGFUSE_PUBLIC_KEY=votre_clé_langfuse
LANGFUSE_SECRET_KEY=votre_secret_langfuse
```
(Attention, parfois les clés sont utilisés directement dans le .env sans même être appelés dans le code)

## 🚀 Utilisation

1. Démarrer le serveur :
```bash
poetry run uvicorn main:app --reload
```

2. Accéder à l'API :
- L'API est disponible sur `http://localhost:8000`
- Documentation Swagger sur `http://localhost:8000/docs`

## 📝 Endpoints

### POST /
Analyse un document PDF et génère une synthèse avec audio.

Paramètres :
- `file` : Fichier PDF à analyser
- `user_prompt` : Prompt personnalisé pour l'analyse

## 🖥️ Frontend

Le frontend est développé avec Next.js et offre une interface utilisateur moderne et réactive.

### Technologies Frontend
- Next.js 15.2.4
- React 19
- TypeScript
- TailwindCSS
- PDF.js pour la visualisation des PDF

### Installation du Frontend
```bash
cd frontend
pnpm install
```

### Démarrage du Frontend
```bash
pnpm dev
```
Le frontend sera disponible sur `http://localhost:3000`

### Fonctionnalités Frontend
- Interface utilisateur intuitive pour le téléchargement de PDF
- Visualisation des PDF directement dans le navigateur
- Gestion des prompts personnalisés
- Lecture de la synthèse vocale
- Affichage des résultats d'analyse structurés

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

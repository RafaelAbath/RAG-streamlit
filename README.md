# Chatbot PDF com RAG (Retrieval-Augmented Generation)

Este projeto é uma aplicação de **Chatbot** que utiliza **RAG (Retrieval-Augmented Generation)** para interagir com documentos PDF. O chatbot permite que o usuário faça upload de seus documentos e receba respostas baseadas no conteúdo desses arquivos.

## Tecnologias Utilizadas

- **LangChain**: Framework que facilita a construção de aplicações LLM (Modelos de Linguagem de Grande Escala) integradas com fontes externas de dados.
- **Qdrant**: Banco de dados de vetores utilizado para armazenar embeddings dos documentos PDF, permitindo uma busca eficiente e rápida.
- **RAG (Retrieval-Augmented Generation)**: Técnica que combina a recuperação de informações externas com a geração de texto, proporcionando respostas mais contextuais e informadas.
- **Streamlit**: Framework utilizado para criar a interface do usuário para o chatbot.
- **Python 3.x**: Linguagem de programação utilizada para desenvolver a aplicação.

## Funcionalidades

- **Upload de Documentos PDF**: O usuário pode fazer upload de documentos PDF para que o chatbot possa processá-los.
- **Busca Contextual**: Após o upload dos PDFs, o chatbot pode buscar informações específicas dentro dos documentos e fornecer respostas relevantes.
- **Resposta Interativa**: O chatbot responde a perguntas baseadas no conteúdo extraído dos documentos, utilizando **RAG** para melhorar a precisão das respostas.
- **Armazenamento de Dados**: Os dados extraídos dos documentos são armazenados e indexados para facilitar a recuperação e a interação durante o processo de consulta.

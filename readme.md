# DocuMind – Document QA System

A conversational document question-answering system that allows users to upload PDF files and ask questions about their content using advanced AI. DocuMind leverages semantic search with FAISS vector embeddings and the Groq Llama 3.3 70B model for accurate, context-aware responses.

## Features

- **PDF Upload & Processing**: Extract text from PDF documents automatically
- **Semantic Search**: Uses sentence-transformers to create dense vector embeddings for efficient document retrieval
- **Fast Retrieval**: FAISS-powered vector indexing for quick document chunk retrieval
- **Advanced QA**: Powered by Groq's Llama 3.3 70B model for high-quality answers
- **Context-Aware Responses**: Answers are generated only from uploaded document content
- **Interactive UI**: Built with Streamlit for an intuitive user experience

## Prerequisites

- Python 3.8+
- A Groq API key (get one at [console.groq.com](https://console.groq.com))

## Installation

1. Clone or navigate to the project directory:
```bash
cd documind
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

Start the Streamlit application:
```bash
streamlit run app.py
```

The app will open in your browser. Follow these steps:

1. Upload a PDF document using the file uploader
2. Wait for the document to be processed (text extraction and vectorization)
3. Once processed, ask questions about the document in the text input field
4. View the AI-generated answer and the retrieved context chunks

## Project Structure

```
documind/
├── app.py                      # Main Streamlit application
├── document_processor.py       # PDF loading and text chunking
├── vector_store.py            # FAISS vector store management
├── qa_engine.py               # LLM-based question answering
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## How It Works

1. **Document Processing**: PDFs are parsed and split into overlapping text chunks (800 characters with 200-character overlap)
2. **Embedding**: Each chunk is converted to a semantic vector using the MiniLM sentence transformer
3. **Indexing**: Vectors are stored in a FAISS index for fast similarity search
4. **Retrieval**: When a question is asked, it's embedded and the 3 most similar chunks are retrieved
5. **Generation**: Retrieved chunks are sent to Llama 3.3 70B via Groq API for context-aware answer generation

## Dependencies

- **streamlit**: Web UI framework
- **pypdf**: PDF text extraction
- **faiss-cpu**: Vector similarity search
- **sentence-transformers**: Semantic embeddings (MiniLM-L6-v2 model)
- **openai**: LLM utilities
- **torch**: Deep learning framework
- **scikit-learn**: Machine learning utilities
- **groq**: Groq API client

See `requirements.txt` for full dependency list.

## Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key (required)

### Tunable Parameters

In `document_processor.py`:
- `chunk_size`: Size of text chunks (default: 800 characters)
- `overlap`: Overlap between chunks (default: 200 characters)

In `vector_store.py`:
- `k`: Number of retrieved chunks for context (default: 3 in search method)

## Performance Notes

- First document processing may take a moment due to model loading
- The Llama 3.3 70B model on Groq provides excellent reasoning capabilities for complex documents
- FAISS uses L2 distance for semantic similarity matching

## Limitations

- Answers are limited to information present in the uploaded document
- For documents with complex layouts or scans, text extraction quality depends on PDF structure
- Processing large documents (500+ pages) may take additional time for embedding generation

## Future Improvements

- Support for multiple documents in a single session
- Document summarization feature
- Export chat history
- Batch processing for multiple PDFs
- Advanced filtering options (search by date, source, etc.)

## License

This project is provided as-is for educational and commercial use.

## Support

For issues or questions about Groq API integration, visit [console.groq.com](https://console.groq.com).


Full logic flow summary

User Uploads PDF
        ↓
Extract Text
        ↓
Split into chunks
        ↓
Generate embeddings
        ↓
Store in FAISS index
--------------------------------
User asks question
        ↓
Generate question embedding
        ↓
Retrieve top-k similar chunks
        ↓
Send chunks + question to LLM
        ↓
LLM generates grounded answer
        ↓
Return answer + context
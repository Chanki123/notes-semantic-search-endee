
# Semantic Search for Study Notes using Endee Vector Database

This project implements a semantic search system for study notes using the Endee vector database.

# Semantic Search for Study Notes using Endee Vector Database

## Overview
This project implements a semantic search system for study notes using the Endee vector database.
Instead of traditional keyword-based search, it retrieves notes based on their semantic meaning.

## Problem Statement
Students often struggle to find relevant information in large collections of study notes.
Keyword search fails when different words are used for the same concept.
This project solves that problem using vector-based semantic search.

## System Architecture
1. Study notes are ingested and split into chunks
2. Each chunk is converted into a vector embedding
3. Embeddings are stored in the Endee vector database
4. User queries are converted into embeddings
5. Endee performs similarity search to return relevant notes

## Role of Endee
Endee is used as the vector database to store embeddings of study notes and perform efficient
semantic similarity search.

## Tech Stack
- Python
- Embedding model (to generate vectors)
- Endee Vector Database

## Project Structure
notes-semantic-search-endee/
├── README.md
├── requirements.txt
├── data/
│ └── notes.txt
├── ingest_notes.py
├── search_notes.py
└── config.py


## Current Status
Endee platform access is currently under early-access waitlist.
The project structure and logic are prepared to enable immediate integration
once access is granted.

## Future Enhancements
- RAG-based question answering
- Web interface for students
- Support for PDF notes

## How It Works (Example)
Query: "laws related to electrical circuits"

Returned Notes:
- Ohm’s Law
- Kirchhoff’s Voltage Law



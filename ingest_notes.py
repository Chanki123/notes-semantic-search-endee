"""
This script ingests study notes, generates embeddings,
and stores them in the Endee vector database.
"""

def load_notes(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().split("\n\n")


def generate_embedding(text):
    # Placeholder for embedding model
    return [0.0] * 768


def store_in_endee(chunks):
    for chunk in chunks:
        embedding = generate_embedding(chunk)
        # TODO: Store embedding in Endee
        print("Prepared note chunk:", chunk[:50])


if __name__ == "__main__":
    notes = load_notes("data/notes.txt")
    store_in_endee(notes)

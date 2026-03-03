import os
import chromadb
from chromadb.config import Settings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db")

DATA_DIR = os.path.dirname(os.path.dirname(__file__))

STROKE_FILE = os.path.join(DATA_DIR, "stroke_india.txt")
CARDIAC_FILE = os.path.join(DATA_DIR, "cardiac_chunks.txt")

CHUNK_SIZE = 500


def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def split_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks


def main():

    print("Starting knowledge loading...")
    print("CHROMA DB PATH:", CHROMA_PATH)
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    collection = client.get_or_create_collection(
        name="medical_knowledge"
    )

    stroke_text = load_file(STROKE_FILE)
    cardiac_text = load_file(CARDIAC_FILE)
    print("Stroke file length:", len(stroke_text))
    print("Cardiac file length:", len(cardiac_text))
    stroke_chunks = split_text(stroke_text, CHUNK_SIZE)
    cardiac_chunks = split_text(cardiac_text, CHUNK_SIZE)

    all_chunks = stroke_chunks + cardiac_chunks

    print("Total chunks:", len(all_chunks))

    ids = [f"doc_{i}" for i in range(len(all_chunks))]

    collection.add(
    documents=all_chunks,
    ids=ids
    )
    print("Documents stored:", collection.count())
    print("Knowledge base created successfully!")


if __name__ == "__main__":
    main()
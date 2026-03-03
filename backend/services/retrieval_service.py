# services/retrieval_service.py
import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("medical_knowledge")


def retrieve_context(symptoms, n_results: int = 2):

    results = collection.query(
        query_texts=[symptoms],
        n_results=n_results
    )

    docs = results["documents"][0]
    distances = results["distances"][0]

    cleaned_docs = []

    print("\nRETRIEVED DOCUMENTS:")
    for d in docs:
        print("---------------------")
        print(d[:600])

        d = d.replace("Chunk", "")
        d = d.replace("Clinical Context:", "")
        d = d.replace("Doctor Action Steps:", "")
        d = d.replace("Emergency Level:", "")
        d = d.replace("\r", " ")
        d = " ".join(d.split())

        cleaned_docs.append(d.strip())

    context = "\n\n".join(cleaned_docs)

    # ----- confidence calculation -----
    avg_distance = sum(distances) / len(distances)
    confidence = round(1 - avg_distance, 2)

    print("CONFIDENCE SCORE:", confidence)

    return context, confidence
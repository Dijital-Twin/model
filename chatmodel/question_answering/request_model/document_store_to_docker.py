from haystack.nodes import EmbeddingRetriever, PreProcessor
from haystack.document_stores import WeaviateDocumentStore
import os

print("Import Successfully")

# Change path with your summary path
# Summary is available in "../friends/summary", or drive link is available in README file
path_to_summaries = "../friends/summary"

final_doc = []

for root, dirs, files in os.walk(path_to_summaries):
    for file in files:
        print(file)
        with open(file, 'r') as file:
            content = file.read()
            new_doc = {
                'content': content,
                'meta': {'path': file}
            }
            final_doc.append(new_doc)
    
document_store = WeaviateDocumentStore(host='http://localhost',
                                       port=8080,
                                       embedding_dim=384)

preprocessor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=False,
    clean_header_footer=True,
    split_by="word",
    split_length=500,
    split_respect_sentence_boundary=True,
)

preprocessed_docs = preprocessor.process(final_doc)

document_store.write_documents(preprocessed_docs)

retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",
)

document_store.update_embeddings(retriever)

print("Embeddings Done.")
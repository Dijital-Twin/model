from haystack.nodes import PromptNode
from haystack.nodes import EmbeddingRetriever, FARMReader
from haystack.document_stores import WeaviateDocumentStore
from haystack import Pipeline

import json
import sys

# load_dotenv()

def get_result(query):
    document_store = WeaviateDocumentStore(
        host='http://localhost',
        port=8080,
        embedding_dim=384
    )

    prompt_node = PromptNode(model_name_or_path="FacebookAI/roberta-base", model_kwargs={'task_name':'text2text-generation'})

    retriever = EmbeddingRetriever(
        document_store=document_store,
        embedding_model="sentence-transformers/all-MiniLM-L6-v2"
    )

    query_pipeline = Pipeline()

    fine_tuned_qa_model_path = "/Users/gurcan/Desktop/Bitirme/haystackconnect/haystackservice/Haystack-and-Mistral-7B-RAG-Implementation/model3/my_model_3epoch"

    reader = FARMReader(model_name_or_path=fine_tuned_qa_model_path, use_gpu=False)
    query_pipeline.add_node(component=retriever, name="Retriever", inputs=["Query"])
    query_pipeline.add_node(component=prompt_node, name="PromptNode", inputs=["Retriever"])
    query_pipeline.add_node(component=reader, name="Reader", inputs=["PromptNode"])

    json_response = query_pipeline.run(query=query, params={"Retriever": {"top_k": 5}, "Reader": {"top_k": 3}})
    
    prediction = [x.to_dict() for x in json_response["answers"]]

    sorted_predictions = sorted(prediction, key=lambda x: x['score'], reverse=True)
    best_answer = sorted_predictions[0]['answer']
    best_answer_score = sorted_predictions[0]['score']
    best_answer_context = sorted_predictions[0]['context']

    updated_answer = best_answer
    relevant_documents = f"{best_answer_score}  {best_answer_context}"
    return updated_answer, relevant_documents

question = json.loads(sys.argv[1])

answer, relevant_documents = get_result(question)
print(json.dumps({"answer": answer, "relevant_documents": relevant_documents}))

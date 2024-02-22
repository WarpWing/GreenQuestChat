# GreenQuestChat Repository
GreenQuestChat or "Gaia" is a RAG System Agent that allows users to ask in-depth queries about Dickinson College's sustainability practices and GreenQuest Solutions business records. This system utilizes LLama Index to find context in unstructured data(PDFs, Text Files) through a process called Retrieval Augmented Generation or RAG. Gaia runs on GPT-4 for a base model and then uses Qdrant (Vector Search Engine) for storing documents with VoyageAI's [Voyage Lite 2 Instruct Embeddings](https://docs.voyageai.com/embeddings/) as per top ranking performance on the [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard). At this point, Gaia is currently self-hosted on a HA Kubernetes Cluster with NGINX for traffic routing and updates through ArgoCD via webhook state. Created originally for Professor Xiaolu Wang's INBM 100 class, now serves as a side project.

Check out Gaia running here: https://gaia.warpwing.cloud/

> [!NOTE]  
> Data covered in this repository is only a public subset of what GQChat or "Gaia" has access to. The data in the repository serves as a small test example. It should be also be noted that some of this data is old and mentions 2023 as "the future".

# Topics Covered 
- Center for Sustainability Education (CSE)
- Alliance for Aquatic Resource Monitoring (ALLARM)
- Dickinson College's Strategic Plans for Climate Change and Climate Objectives 
- Living Lab Overview (The Hive, Treehouse, Handlebar, Dickinson College Organic Farm)
- Anything related to Sustainability at Dickinson (Other topics outside of the mentioned above)
> [!WARNING]  
> GPT-4 isn't perfect and still has risks of hallucinations. All listed topics are implemented but not guaranteed to be as succinct as a human response.

# To Do List 
- [ ] Benchmark Mistral 8x7b vs GPT4 on Gaia Dataset. While GPT4 is better, Mistral 8x7b could be better for cost if Mistral has sufficient answering capabilities. Both are Sparse MoE anyways.
- [ ] Work on implementing KnowledgeGraphs instead of Vector Search Engines for more accurate queries.
- [ ] Look into Query Routing based on Query Type. View [this](https://docs.llamaindex.ai/en/stable/examples/query_engine/RouterQueryEngine.html#) for future reference.
- [ ] Look into testing frameworks for RAG pipelines. I would like to use [Ragas](https://docs.ragas.io/en/stable/index.html) but still evaluating metrics and working on writing proper Q/A sets for datasets. It's on the backburner
- [ ] Figuring out how to get Gaia to recognize acronyms within the context. For example, CSE in Gaia's context should stand for "Center for Sustainability Education" but Gaia registers it as "Computer Science and Engineering".
- [ ] Retest and Evaluate Embeddings and Vector Params. I probably will migrate to [SalesForce's Mistral Embeddings](https://huggingface.co/Salesforce/SFR-Embedding-Mistral) but that requires me to change the vector dimensions to 4096. This should be fine as long as I reconfigure the Qdrant Collection to accept Vectors of that size. I also would need to download the HuggingFace embeddings locally which should be fine, it just requires some testing and infrastructure changes.
- [ ] Possibly rework the UI? It's meant to be simplistic and I have a hard limit on my OpenAI key. I'll possibly look into it.
  


# Example LLM Chain Response
![image](https://github.com/WarpWing/GreenQuestChat/assets/28925758/1fcd5ca6-c42b-4770-bf98-ec53d6b57979)

# Example Outputs
![image](https://github.com/WarpWing/GreenQuestChat/assets/28925758/878bb681-7c01-450a-9cc6-c9c8d1addb52)
![image](https://github.com/WarpWing/GreenQuestChat/assets/28925758/ee2cccd3-4a98-467b-a773-9f8258b03fb5)
![image](https://github.com/WarpWing/GreenQuestChat/assets/28925758/25502bbf-a117-4d4a-af0d-04e783473ae1)




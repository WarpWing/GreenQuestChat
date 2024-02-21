# GreenQuestChat Repository
GreenQuestChat or "Gaia" is a RAG System Agent that allows users to ask in-depth queries about Dickinson College's sustainability practices and GreenQuest Solutions business records. This system utilizes LLama Index to find context in unstructured data(PDFs, Text Files) through a process called Retrieval Augmented Generation or RAG. Gaia runs on GPT-4 for a base model and then uses Qdrant (Vector Search Engine) for storing documents with VoyageAI's [Voyage Lite 1 Instruct Embeddings](https://docs.voyageai.com/embeddings/) as per top ranking performance on the [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) as of 12/20/2023. At this point, Gaia is currently self-hosted on a HA Kubernetes Cluster utilizing the NGINX Ingress Gateway for traffic routing.

> [!NOTE]  
> Data covered in this repository is only a public subset of what GQChat or "Gaia" has access to. The data in the repository serves as a small test example.

# Topics Covered 
- Center for Sustainability Education (CSE)
- Alliance for Aquatic Resource Monitoring (ALLARM)
- Dickinson College's Strategic Plans for Climate Change and Climate Objectives 
- Living Lab Overview (The Hive, Treehouse, Handlebar, Dickinson College Organic Farm, et al)
> [!WARNING]  
> GPT-4 isn't perfect and still has risks of hallucinations. All listed topics are implemented but not guaranteed to be as succinct as a human response.

# To Do List

# Demo
Check out Gaia running here: https://gaia.warpwing.cloud/

# Example Outputs
![image](https://github.com/WarpWing/GreenQuestChat/assets/28925758/878bb681-7c01-450a-9cc6-c9c8d1addb52)
![image](https://github.com/WarpWing/GreenQuestChat/assets/28925758/ee2cccd3-4a98-467b-a773-9f8258b03fb5)
![image](https://github.com/WarpWing/GreenQuestChat/assets/28925758/25502bbf-a117-4d4a-af0d-04e783473ae1)


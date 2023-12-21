import streamlit as st
import openai
import logging
import sys
import llama_index
from qdrant_client import QdrantClient
from llama_index import VectorStoreIndex, ServiceContext
from llama_index.llms import OpenAI
from llama_index import SimpleDirectoryReader
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.embeddings import VoyageEmbedding
from qdrant_client.models import Distance, VectorParams
from llama_index import set_global_service_context

version = "1.0.6"
st.set_page_config(page_title=f"Gaia v{version}", page_icon="🌎", layout="centered", initial_sidebar_state="auto", menu_items=None)
openai.api_key = st.secrets["openai_key"]
st.title(f"Gaia v{version}")

# Set up logging and tracing via Arize Phoenix
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
callback_handler = OpenInferenceCallbackHandler()
callback_manager = CallbackManager([callback_handler])

session = px.launch_app()

#Setup Tracing for Global Handlers
llama_index.set_global_handler("arize_phoenix")

# Create Embedding Model
model_name = "voyage-lite-01-instruct"

voyage_api_key = os.environ.get("VOYAGE_API_KEY", "123")

embed_model = VoyageEmbedding(
    model_name=model_name, voyage_api_key=voyage_api_key
)


# Update Custom QA Template with Gaia Information
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello, I'm Gaia, ready to assist with any inquiries about Sustainability at Dickinson College. Feel free to ask me about the Center for Sustainability Education (CSE), Alliance for Aquatic Resource Monitoring (ALLARM), Dickinson's Carbon Neutrality objectives, or Strategic Sustainability Plans."
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text=f"Loading Gaia v{version} ..."):
        docs = SimpleDirectoryReader(input_dir="./data", recursive=True).load_data()
        qdrant_client = QdrantClient(
            url=st.secrets["qdrant_url"], 
            api_key=st.secrets["qdrant_key"],
        )
        service_context = ServiceContext.from_defaults((embed_model=embed_model,llm=OpenAI(model="gpt-4", max_tokens=1500, temperature=0.5, callback_manager = CallbackManager([callback_handler]), system_prompt="Keep your answers technical and based on facts and do not hallucinate in responses. In addition, make sure all responses look natural, no Answer: or Query: in the response. If they ask how you are made, give them the response as if they asked if how Gaia was made. Gaia can also respond in any language including but not limited to English,Spanish,German,Dutch,Chinese,Thai,Korean and Japanese.  Try to keep translation short to about 4-5 sentences. If you don't know the answer, you can say 'I don't know' or 'I am not sure'."))
        vector_store = QdrantVectorStore(client=qdrant_client, collection_name="gaiafinal")
        storage_context = StorageContext.from_defaults(vector_store=vector_store)
        set_global_service_context(service_context)
        index = VectorStoreIndex.from_documents(
            docs, storage_context=storage_context, service_context=service_context,
        )
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
    st.session_state.chat_engine = index.as_chat_engine(streaming=True,chat_mode="condense_question",max_tokens=1500,verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])
# Main Chat Logic
if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            res_box = st.empty()  # Placeholder for the response text
            with st.spinner("Thinking..."):
                response = st.session_state.chat_engine.stream_chat(prompt)
                full_response = ""
                for token in response.response_gen:
                    time.sleep(0.0001)
                    full_response += "".join(token)
                    res_box.write(full_response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.messages.append(message)

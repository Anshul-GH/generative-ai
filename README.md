# generative-ai
Practicing writing Python code for generative AI

yt_streamlit:
https://www.youtube.com/watch?v=RV_MihEQ4BA


pandasai:
https://www.youtube.com/watch?v=BtmMNZLxbuI


gpt-engineer:
https://github.com/AntonOsika/gpt-engineer
https://www.youtube.com/watch?v=FPZONhA0C60


generate images with openai:
https://www.geeksforgeeks.org/generate-images-with-openai-in-python/


extracting data from pdf:
https://www.freecodecamp.org/news/extract-data-from-pdf-files-with-python/



How to setup and use Ollama:
1. Go to https://ollama.com/download and download the installer applicable
2. Run the installer with default settings
3. Once installed, it should available as a command in the terminal (or windows command prompt for windows)
4. Type: >ollama (enter). This should display the various options available
5. Type: >ollama run phi3  (enter). This will download and install the phi3 model.
6. Type: >ollama run mxbai-embed-large  (enter). This will download and install the mxbai-embed-large model.
7. Install python version 3.11.9 (https://www.python.org/downloads/release/python-3119/) [Version 12 has some changes that may cause issues with the current code]
8. Setup python at the 'PATH' environment variable (in case of windows. May not be needed for mac/linux)
9. Make sure that python is installed
> python  (enter)
This is provide python environment details and options available
10. Create a project directory and create a virtual environment at that path:
> <directory_path>python -m venv /path/to/new/virtual/environment(for example, llm)  (enter)
11. Copy the file 'ollama_embeddings.py' to a desired project path and open the same in a terminal.
12. Create a new virtual environment at the project path:
> python -m venv /path/to/new/virtual/environment  (enter)
13. Install the requirements files at the project path within the virtual environment:
(llm)> pip install -r /path/to/requirements.txt
14. Inside the project path, create a source (src) folder to store the context/reference data file and copy the file there.
{llm)> mkdir src  (enter)
15. Execute the python code:
> python ollama_embeddings.py
16. If everything was setup correctly, it will generate embeddings at project_path\embeddings\ location. Also the llm chat will activate and ready to be asked a question ("What do you want to know? -> ")
17. Ask a relevant questions and the llm will respond.
18. Depending on the system, it may take some time to both generate embeddings and also responding to the question.
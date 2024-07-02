import ollama
import os
import json
import numpy as np
import constants as const
from numpy.linalg import norm
from model import LargeLangModel

def main():

    # create an LLM model class object
    llm_object = LargeLangModel()

    # open file
    filename = const.CTX_FILENAME
    filepath = const.CTX_FILEPATH
    paragraphs = llm_object.parse_file(filepath)
    
    embeddings = llm_object.get_embeddings(filename, const.EMBED_MODEL_NAME, paragraphs)

    prompt = input("What do you want to know? -> ")
    prompt_embedding = ollama.embeddings(model=const.EMBED_MODEL_NAME, prompt=prompt)['embedding']

    # find most similar to each other
    most_similar_chunks = llm_object.find_most_similar(prompt_embedding, embeddings)[:5]
    # for item in most_similar_chunks:
    #     print(item[0], paragraphs[item[1]])

    if most_similar_chunks:
        response = ollama.chat(
            model=const.CHAT_MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": const.SYSTEM_PROMPT
                    + "\n".join(paragraphs[item[1]] for item in most_similar_chunks),
                },
                {
                    "role": "user",
                    "content": prompt
                },
            ]
        )
        print("\n\n")
        print(response["message"]["content"])
    else:
        print("Model could not find the answer from the context provided.")


if __name__ == "__main__":
    main()

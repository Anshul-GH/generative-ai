import os
import json
import ollama
import numpy as np
from numpy.linalg import norm


class LargeLangModel:
    """ Custom LLM model class.
    """
    
    def __init__(self) -> None:
        """Constructor"""
        pass

    def parse_file(self, filename):
        with open(filename, encoding="utf-8-sig") as f:
            paragraphs = []
            buffer = []
            for line in f.readlines():
                line = line.strip()
                if line:
                    buffer.append(line)
                elif len(buffer):
                    paragraphs.append((' ').join(buffer))
                    buffer  = []
            if len(buffer):
                paragraphs.append((' ').join(buffer))
        return paragraphs

    def save_embeddings(self, filename, embeddings):
        # create the directory if it doesn not exists
        if not os.path.exists("embeddings"):
            os.mkdir("embeddings")
        
        # dump embeddings to json
        with open(f"embeddings\{filename}.json", 'w') as f:
            json.dump(embeddings, f)

    def load_embeddings(self, filename):
        # check if the file exists
        if not os.path.exists(f"embeddings\{filename}.json"):
            return False
        
        # load embeddings from json
        with open(f"embeddings/{filename}.json", "r") as f:
            return json.load(f)

    def get_embeddings(self, filename, modelname, chunks):
        # check if embeddings are already saved
        if (embeddings := self.load_embeddings(filename)) is not False:
            return embeddings
        # get embeddings from ollama
        embeddings = [
            ollama.embeddings(model=modelname, prompt=chunk)['embedding']
            for chunk in chunks
        ]

        # save embeddings
        self.save_embeddings(filename, embeddings)

        return embeddings

    def find_most_similar(self, needle, haystack):
        needle_norm = norm(needle)
        similarity_scores = [
            np.dot(np.asarray(needle), item) / (needle_norm * norm(item)) for item in haystack
        ]

        return sorted(zip(similarity_scores, range(len(haystack))), reverse=True)

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import DatasetDict
import pandas as pd
from datasets import load_dataset

class LLM_classifier:
    def __init__(self, llm_model_name: str, corpus_name: str):       
        #Loading LLM
        if llm_model_name != "":
            self.LLM_model, self.LLM_tokenizer = self.load_llm(llm_model_name, corpus_name)

    def load_llm(self, model_name: str, corpus_name: str)-> tuple:
        LLM_model = AutoModelForCausalLM.from_pretrained(model_name,
                                            load_in_4bit=True,
                                            bnb_4bit_compute_dtype=torch.bfloat16,
                                            torch_dtype=torch.float16,
                                            device_map="auto"
                                            )
        LLM_tokenizer = AutoTokenizer.from_pretrained(model_name)

        self.labels_topos, self.definitions_topos_list, self.definitions_topos = self.set_labels(corpus_name)
        self.dataset = self.set_dataset(corpus_name)

        return LLM_model, LLM_tokenizer

    def set_labels(self, corpus: str) -> list:
        df_topos= pd.read_csv(f"./topos.csv")

        labels_topos = df_topos.label.tolist()
        definitions_topos_list = df_topos.definition.tolist()
        definitions_topos = {label : definition for label, definition in zip(labels_topos, definitions_topos_list)}

        return labels_topos, definitions_topos_list, definitions_topos

    def set_dataset(self, corpus_name) -> DatasetDict:
        dataset = load_dataset("ronunes/anacreontea")

        return dataset

    def get_definitions(self, labels, definitions):
        definitions_str = ""

        for idx, label in enumerate(labels):
            definitions_str += f'- "{label}": {definitions[label]}\n'

        return definitions_str
    
    def list_to_string_with_quotes(self, lst):
        # Check if the list is not empty
        if not lst:
            return ""
        
        # Add single quotes around each element and join them with commas
        result = ", ".join(f"'{value}'" for value in lst)
        
        # Replace the last comma with 'and' for proper formatting
        last_comma_index = result.rfind(", ")
        if last_comma_index != -1:
            result = result[:last_comma_index] + " e " + result[last_comma_index + 2:]
        
        return result
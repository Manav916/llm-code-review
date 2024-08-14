# Import necessary libraries
from transformers import AutoConfig, AutoModelForSequenceClassification, AutoTokenizer, pipeline
import gensim

def preprocess(issue_title, issue_body):
    # concatenate title and body, then remove whitespaces
    doc = ""
    doc += str(issue_title)
    doc += " "
    doc += str(issue_body)
    doc = gensim.parsing.preprocessing.strip_multiple_whitespaces(doc)
    return doc

def label_issue(issue_title, issue_body):
    issue_data = preprocess(issue_title, issue_body)
    # Load the original configuration
    config = AutoConfig.from_pretrained('PeppoCola/IssueReportClassifier-NLBSE22')

    # Define new label mappings
    new_id2label = {0: "bug", 1: "enhancement", 2: "question"}
    new_label2id = {"bug": 0, "enhancement": 1, "question": 2}

    # Update the configuration
    config.id2label = new_id2label
    config.label2id = new_label2id

    # Load the model with the updated configuration
    model = AutoModelForSequenceClassification.from_pretrained('PeppoCola/IssueReportClassifier-NLBSE22', config=config)
    tokenizer = AutoTokenizer.from_pretrained('PeppoCola/IssueReportClassifier-NLBSE22')

    # Create the pipeline with the modified model
    classifier = pipeline("text-classification", 
                        model=model,
                        tokenizer=tokenizer,
                        add_special_tokens=True,
                        padding='longest',
                        truncation=True)

    results = classifier(issue_data)
    return results[0]['label']


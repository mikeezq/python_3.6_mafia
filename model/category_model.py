import string
import torch
import torch.nn as nn

from transformers import AutoTokenizer, AutoModel


class GradTextModel(nn.Module):
    def __init__(self, bert, labels_number):
        super().__init__()
        self.bert = bert
        self.fc = nn.Sequential(
            nn.GELU(),
            nn.Linear(312, labels_number)
        )

    def forward(self, x):
        bert_output = self.bert(**x)
        return self.fc(bert_output.last_hidden_state[:, 0, :])


def get_model_tokenizer(path):
    tokenizer3 = AutoTokenizer.from_pretrained("cointegrated/rubert-tiny")
    bert3 = AutoModel.from_pretrained("cointegrated/rubert-tiny")

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    modelg = GradTextModel(bert3, 3105)
    modelg.load_state_dict(torch.load(path, map_location=device))
    modelg = modelg.eval()

    return modelg, tokenizer3


def preprocess_name(name):
    punct_translation = str.maketrans('', '', string.punctuation)
    return name.lower().translate(punct_translation)


def out_to_names(out, le, codes_dict, n=5):
    s_inds = out.argsort(descending=True)[0, :n].tolist()
    codes = le.inverse_transform(s_inds)
    return [codes_dict[ind].capitalize() for ind in codes]


def topn(req, tokenizer, model, le, codes_dict, n=5):
    text = preprocess_name(req)
    tokenized = tokenizer(text, return_tensors='pt')
    model_output = model(tokenized)
    return out_to_names(model_output, le, codes_dict, n)

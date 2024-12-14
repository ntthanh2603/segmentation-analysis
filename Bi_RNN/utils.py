import os
import yaml
import math
import numpy as np
from datetime import datetime
import torch
import torchtext.vocab as vocab
from torch.utils.data import random_split
from torch.utils.tensorboard import SummaryWriter
from RNN import RNN
from Vocabulary import Vocabulary
from IMDBDataset import IMDBDataset


def get_config(file_path):
    with open(file_path, "r") as f:
        config = yaml.safe_load(f)
    return config

def get_pretrained_word2vec(fpath):
    return vocab.Vectors(name=fpath, unk_init=torch.Tensor.normal_)

def create_vocab_from_word2vec(word_embedding):
    vocab = Vocabulary()

    # create vocabulary from pretrained word2vec
    words_list = list(word_embedding.stoi.keys())
    for word in words_list:
        vocab.add(word)

    return vocab

def get_vocab_and_word2vec(config, log_dir):
    word_embedding = get_pretrained_word2vec(config["model"]["embedding_fpath"])
    load_fpath = config["vocab"]["load_fpath"]

    if load_fpath is not None:
        vocabulary = torch.load(load_fpath)
    else:
        vocabulary = create_vocab_from_word2vec(word_embedding)

    if config["vocab"]["save"]:
        torch.save(vocabulary, f"{log_dir}/vocab.pt")

    return vocabulary, word_embedding

def get_dataset(config, vocabulary, log_dir):
    """Load the full dataset and return train, validate and test sets"""
    dataset = IMDBDataset(vocabulary, 
                          config["dataset"]["csv_fpath"],
                          config["dataset"]["tokenized_fpath"])

    if config["dataset"]["tokenized_save"]:
        torch.save(dataset.tokenized_reviews, f"{log_dir}/tokenized.pt")
  
    return dataset, split_dataset(dataset, config["dataset"]["split_rate"])

def get_model(config, vocabulary, word_embedding):
    embedding_dim = config["model"]["embedding_dim"]
    hidden_dim = config["model"]["hidden_dim"]
    n_layers = config["model"]["n_layers"]
    bidirectional = config["model"]["bidirectional"]
    dropout = config["model"]["dropout"]

    input_dim = word_embedding.vectors.shape[0]
    pad_idx = vocabulary["<pad>"]
    unk_idx = vocabulary["<unk>"]

    model = RNN(input_dim, 
                embedding_dim, 
                hidden_dim,  
                n_layers, 
                bidirectional, 
                dropout, 
                pad_idx)

    model.embedding.weight.data.copy_(word_embedding.vectors)
    model.embedding.weight.data[unk_idx] = torch.zeros(embedding_dim)
    model.embedding.weight.data[pad_idx] = torch.zeros(embedding_dim)

    return model

def split_dataset(dataset, split_rate):
    full_size = len(dataset)
    train_size = (int)(split_rate * full_size)
    valid_size = (int)((full_size - train_size)/2)
    test_size = full_size - train_size - valid_size
    return random_split(dataset, lengths=[train_size, valid_size, test_size])

def create_dir(dpath):
    is_exist = os.path.exists(dpath)
    if not is_exist:
        os.makedirs(dpath)

def create_current_log_dir(logs_dir):
    this_time = datetime.now().strftime("%Y%m%d-%H%M%S")
    current_log_dir = f"{logs_dir}/{this_time}"
    create_dir(current_log_dir)
    state_dir = f"{current_log_dir}/state"
    create_dir(state_dir)
    return current_log_dir, state_dir

def create_logs_dir(config):
    logs_dir = config["train"]["logs_dir"]
    if logs_dir is None:
        logs_dir = "logs"
    create_dir(logs_dir)
    return create_current_log_dir(logs_dir)

def get_writer(log_dir):
    tensorboard_dpath = f"{log_dir}/tensorboard" 
    create_dir(tensorboard_dpath)
    return SummaryWriter(log_dir=tensorboard_dpath)

def binary_accuracy(preds, y):
    """
    Returns accuracy per batch, i.e. if you get 8/10 right, this returns 0.8, NOT 8
    @param preds (torch.Tensor): shape = [batch_size]
    @param y (torch.Tensor): shape = [batch_size]
    @return acc (torch.Tensor): shape = [1]
    """
    #round predictions to the closest integer
    rounded_preds = torch.round(torch.sigmoid(preds))
    correct = (rounded_preds == y).float() #convert into float for division 
    acc = correct.sum() / len(correct)
    return acc

def batch_iterator(dataset, batch_size, pad_idx, device):
    """ Yield the reviews and sentiments of the dataset in batches
    @param dataset (IMDBDataset)
    @param batch_size (int)
    @param pad_idx (int)
    @param device (torch.device)
    @yield dict {"reviews": tuple(torch.Tensor, torch.Tensor), "sentiments": torch.Tensor} 
    """
    batch_num = math.ceil(len(dataset) / batch_size)
    index_array = list(range(len(dataset)))

    np.random.shuffle(index_array)

    for i in range(batch_num):
        indices = index_array[i * batch_size: (i + 1) * batch_size]
        examples = [dataset[idx] for idx in indices]

        examples = sorted(examples, key=lambda e: len(e[0]), reverse=True)

        reviews = [e[0] for e in examples]
        reviews = torch.nn.utils.rnn.pad_sequence(reviews, 
                                                  batch_first=False, 
                                                  padding_value=pad_idx).to(device)
        reviews_lengths = torch.tensor([len(e[0]) for e in examples])
        sentiments = torch.tensor([e[1] for e in examples]).to(device)

        yield {"reviews": (reviews, reviews_lengths), "sentiments": sentiments} 

def epoch_time(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time / 60)
    elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
    return elapsed_mins, elapsed_secs
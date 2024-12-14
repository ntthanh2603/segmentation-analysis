import argparse

import torch

import utils
from RNN import RNN

def main(config_fpath, sentence):
    config = utils.get_config(config_fpath)

    model = torch.load(config["model_fpath"])
    vocab = torch.load(config["vocab_fpath"])

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    model.eval()
    corpus = [sentence]
    tensor = vocab.corpus_to_tensor(corpus)[0].to(device)
    tensor = tensor.unsqueeze(1)
    length = [len(tensor)]
    length_tensor = torch.LongTensor(length)
    prediction = torch.sigmoid(model(tensor, length_tensor))
    
    print(prediction.item())
    return prediction.item()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Using model to predict the sentiment of the sentence")

    parser.add_argument("--config", 
                        default="configs/predict_config.yml", 
                        help="path to config file",
                        dest="config_fpath")

    parser.add_argument("--sent", 
                        help="input sentence",
                        dest="sentence")
    
    args = parser.parse_args()

    main(**vars(args))
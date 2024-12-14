# Vietnamese Sentiment Analysis
[![Python 3.8.10](https://img.shields.io/badge/python-3.8.10-blue)](https://www.python.org/downloads/release/python-3107/)
[![PyTorch 1.13.1](https://img.shields.io/badge/PyTorch-1.13.1-red)](https://pypi.org/project/torch/1.13.1/)
[![Torchtext 0.14.1](https://img.shields.io/badge/Torchtext-0.14.1-red)](https://pypi.org/project/torchtext/0.14.1/)
[![Pandas 1.5.3](https://img.shields.io/badge/Pandas-1.5.3-green)](https://pypi.org/project/pandas/1.5.3/)
[![tqdm 4.64.1](https://img.shields.io/badge/tqdm-4.64.1-orange)](https://pypi.org/project/tqdm/)
[![numpy 1.24.1](https://img.shields.io/badge/numpy-1.24.1-green)](https://pypi.org/project/numpy/1.24.1/)
[![underthesea 6.0.3](https://img.shields.io/badge/underthesea-6.0.3-blue)](https://pypi.org/project/underthesea/6.0.3/) 
[![tensorflow 2.11.0](https://img.shields.io/badge/tensorflow-2.11.0-orange)](https://pypi.org/project/tensorflow/2.11.0/) 
[![tensorboard 2.11.2](https://img.shields.io/badge/tensorboard-2.11.2-orange)](https://pypi.org/project/tensorboard/2.11.2/) 

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1NsMMzHGy2EWaJdRtgX-ZbiVNDE2G_dSZ?usp=sharing)  

Build a simple Sentiment Analysis model on the IMDB dataset that has been translated into Vietnamese.

## 1. Setup
After cloning this repository locally, download and extract [this zip file](https://drive.google.com/file/d/1m9tcdIzo3QQETwSOvQM4vIo2d268dY0i/view?usp=share_link), which includes:
- VI_IMDB.csv: includes 50,000 reviews from the IMDB dataset that has been translated into Vietnamese
- vi_word2vec.txt: Pre-trained word2Vec with embedding size of 100 loaded from [PhoW2V](https://github.com/datquocnguyen/PhoW2V)

Then create virtual environment then install required packages:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Usage
This project consists of 3 main activities: training, prediction and observation of results. The training and prediction are set up via configuration files, and the results after each training session are recorded and observed using Tensorboard.

### 2.1. Train the model
We set the parameters for the training process through the `config.yml` file of the following form:
```yml
vocab:
  load_fpath: null
  save: true

dataset:
  csv_fpath: "VI_IMDB.csv"
  tokenized_fpath: null
  tokenized_save: true
  split_rate: 0.8

model:
  embedding_fpath: "vi_word2vec.txt"
  embedding_dim: 100
  hidden_dim: 256
  n_layers: 2
  bidirectional: true
  dropout: 0.5

train:
  n_epochs: 6
  batch_size: 100
  logs_dir: null
  save_epoch: 2

continue:
  state_fpath: null
```

To reduce vocab and dataset loading time, user can save created objects by setting `save` and `tokenized_save` variables to true. The above objects will be saved in the `logs_dir` directory into files, writing the corresponding path to the `load_fpath` and `tokenized_fpath` parameters to save time for the next training.  

The user can continue training by entering the current state file path into the `state_fpath` variable. These files are saved in the `state` folder in `logs_dir`, you can set how often the state is saved during training using `save_epoch`.  

After setting up the `config.yml` file, we run the `train.py` file to start the training process.

```
train.py [-h] [--config CONFIG_FPATH]

optional arguments:
  -h, --help              show this help message and exit
  --config CONFIG_FPATH   path to config file
``` 

Training results and models will be saved in a folder named after the training time in `logs_dir`.

### 2.2. Use the trained model to predict

⚠️ Just like the training process, you need to set up the `predict_config.yml` file before predicting, otherwise the program will return an error result.

```yml
vocab_fpath: null
model_fpath: null
```

The paths to the model and vocab files are in `logs_dir`. After entering the path we proceed to run the file `predict.py` with the sentence to predict sentiment:  

```
predict.py [-h] [--config CONFIG_FPATH] [--sent SENTENCE]

optional arguments:
  -h, --help              show this help message and exit
  --config CONFIG_FPATH   path to config file
  --sent SENTENCE         input sentence
```

The return result is close to 0 if it is a negative review and close to 1 if it is a positive review.

### 2.3. Observe the accuracy and loss of the model

Training is recorded through Tensorboard. To use Tensorboard, run the following command:

```
tensorboard [--logdir LOG_DIR] [--port PORT]
```

Where `LOG_DIR` is the path to the `tensorboard` folder located in the corresponding log folder. Once there, open `http://localhost:{PORT}/`
with {PORT} being the `PORT` value just entered to observe the result.

## 3. References
- https://github.com/bentrevett/pytorch-sentiment-analysis
- https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1214/
- https://github.com/datquocnguyen/PhoW2V
- https://github.com/undertheseanlp/underthesea

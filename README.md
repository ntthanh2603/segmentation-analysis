## Project segmentation-analysis

Sentiment classification of comments provides better understanding of audience reception, supporting filmmakers, streaming platforms, and marketers in making decisions (cutting, adding showtimes, implementing opportunities or campaigns quickly, staying ahead of trends). Sentiment classification faces several challenges: film review language is highly metaphorical, unclear context, etc.

Due to the issues mentioned above, accurate classification requires applying good Natural Language Processing (NLP) techniques to capture more subtle language nuances.

![Image alt text](img/sentiment-analysis.png)
<br>

In this report, we conducted analysis and comparison of two modern deep learning models: Transformer (PhoBERT, DistilBERT) and Bi-RNN (with LSTM layers) for sentiment analysis based on Vietnamese movie reviews.

#### Team Members:

- Nguyen Tuan Thanh - 22022624
- Vu Dinh Tho - 22022580
- Dinh Van Sinh - 22022615
- Nguyen Manh Hung - 22022623
- Nguyen Cong Thanh - 22022630

#### Objectives:

- Build and deploy models: Develop two deep learning models - Transformer and Bi-RNN for sentiment analysis.
- Evaluate and compare: Compare the performance of both models through metrics such as Accuracy, F1-Score, Precision, and Recall.
- Practical applications: Apply analysis results to fields such as customer feedback management, product review monitoring, or social media sentiment surveillance.

#### Data:

Comments from Facebook posts collected using Selenium and PyAutoGUI libraries.
Using Pandas and supporting libraries like emoji, unicodedata, regex, pyvi to convert data to lowercase, Vietnamese word segmentation, Vietnamese word normalization, sentence normalization, link removal, number removal, icon removal, and data visualization.

#### Training:

- Transformer:

  - We will fine-tune and evaluate 2 transformer models using only the Encoder set with the above dataset for sentiment classification. The 2 models used are DistilBERT-base and PhoBERT-base.
  - Hardware used during fine-tuning is 2 T4 GPUs on Kaggle environment. Models will be evaluated through 2 metrics: accuracy and F1 score on the validation set.
    ![Image alt text](img/config-tranformer.png)
  - Models are fine-tuned with learning rate of 2e-5 for 5 epochs, using AdamW optimizer and batch size customized according to the table below.
    ![Image alt text](img/result-tranformer.jpg)
  - After fine-tuning, we found that smaller batch sizes return more accurate results but training time is also longer. PhoBERT model performs better than DistilBERT because PhoBERT is pre-trained on Vietnamese datasets. Due to training resource limitations, we could only evaluate these 2 models.
    ![Image alt text](img/loss-phoBERT.png)

- Bi-RNN:
  - Model parameters:
    - Embedding layer: input_dimension = vocab_size = 1585076, embedding_dimension = 100
    - Dropout = 0.5
    - Hidden layer: using bidirectional
      - Experiments on 2 LSTM layers or 3 LSTM layers
      - hidden_dimension = 100
  - Hyperparameters:
    - Optimizer: experiments with Adam or SGD
    - Batch size: 16, 64, 100
    - Momentum (for SGD): 0.9
    - Learning rate:
      - For Adam: default
      - For SGD: experiments with different learning rates (0.1; 0.01; 0.001)
  - Training conducted using 2 T4 GPUs over 5 epochs. Results of hyperparameter tuning:
    ![Image alt text](img/BiRNN-with- 2class-LSTM.png)
    ![Image alt text](img/BiRNN-with- 3class-LSTM.png)
  - Best loss value of Bi-RNN model (batch size = 64, optimizer = adam)
    ![Image alt text](img/loss-best-model-BiRNN.png)
  - Observations:
    - Increasing batch size leads to reduced training time
    - Increasing learning rate improves model accuracy (for SGD optimizer)
    - Adam optimizer performs better than SGD
    - Model with batch size = 64 gives best results compared to other batch sizes
    - Model with 3 hidden layers achieves higher accuracy than model with 2 hidden layers
    - From the table above, the model with highest accuracy is 95.09% when the model has 3 LSTM layers in hidden layer, batch size = 64, and optimizer = adam

#### General Conclusion:

![Image alt text](img/transformer-birnn.png)

- Bi-RNN outperforms Transformer in both F1-Score (95.14% vs 90.93%) and Accuracy (95.09% vs 90.7%), with approximately 4% difference. This shows that Bi-RNN is more suitable for this problem with the given dataset.
- Transformer may not have reached its full potential, possibly due to insufficient hyperparameter optimization or insufficient data size.
- PhoBERT (Transformer) with highest accuracy of 90.93% is a suitable choice for Vietnamese language processing tasks thanks to its global processing capability and high performance, especially in complex datasets. However, it has limitations when training time is longer compared to Bi-RNN when batch size increases.
- Bi-RNN (with LSTM) with 95.26% accuracy remains a powerful and effective method, especially when training resources are limited. Challenges include long sequences and slower training speed when number of layers increases.
- Results demonstrate the effectiveness of deep learning models in sentiment analysis problems and contribute practically to the development of NLP applications.

#### If there are any errors or improvements needed in the project, or if you have any questions, please contribute your ideas to the issues section of this repo :)).

![#### Thanks for watching!!!](img/thanks-for-watching.jpeg)

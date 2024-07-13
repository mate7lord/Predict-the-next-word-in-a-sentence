from django.shortcuts import render
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

from .sustain import tokenizer

# Create your views here.
def handler(request):
    response = "Input the word first"
    if request.method == 'POST':
        text = request.POST['Name']
        response = predicting(text)
    return render(request, "index.html", {'response': response})


def predicting(data):

    def generate_seq(model, tokenizer, seq_length, seed_text, n_words):
        result = list()
        in_text = seed_text
        # generate a fixed number of words
        for _ in range(n_words):
            # encode the text as integer
            encoded = tokenizer.texts_to_sequences([in_text])[0]
            # truncate sequences to a fixed length
            encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
            # predict probabilities for each word
            predict_x = model.predict(encoded)
            yhat = np.argmax(predict_x, axis=1)
            # map predicted word index to word
            out_word = ''
            for word, index in tokenizer.word_index.items():
                if index == yhat:
                    out_word = word
                    break
            # append to input
            in_text += ' ' + out_word
            result.append(out_word)
        return ' '.join(result)

    # select a seed text
    seed_text = data
    print(seed_text + '\n')
    seq_length = 50
    res_length = 12 # predict next 12 words.
    # load the model
    model = load_model("polls/nextWord.h5")
    Tokenizer = tokenizer
    # generate new text
    generated = generate_seq(model, Tokenizer, seq_length, seed_text, res_length)

    return generated
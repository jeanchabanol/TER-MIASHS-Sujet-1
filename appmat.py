
from distutils.command.clean import clean
import tensorflow as tf
import numpy as np
import streamlit as st
import os

# ML stuff
from transformers import BertTokenizer, TFBertModel
from tensorflow import keras

# preprocessing library
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nlpretext import Preprocessor
from nlpretext.basic.preprocess import normalize_whitespace, lower_text, remove_eol_characters, replace_currency_symbols, \
                                        remove_punct, remove_multiple_spaces_and_strip_text, filter_non_latin_characters
import tensorflow_text as text

# stemmer
stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()

# stopword
stopword_factory = StopWordRemoverFactory()
stopword = stopword_factory.create_stop_word_remover()

def cleanText(sentence):
    # process with PySastrawi first
    stemmed = stemmer.stem(sentence)
    stopwordremoved = stopword.remove(stemmed)

    # then with nlpretext
    cleaned = preprocessor.run(stopwordremoved)

    # return
    return cleaned



# stemmer
stemmer_factory = StemmerFactory()
stemmer = stemmer_factory.create_stemmer()

# stopword
stopword_factory = StopWordRemoverFactory()
stopword = stopword_factory.create_stop_word_remover()

# use nlpretext processor
preprocessor = Preprocessor()
preprocessor.pipe(lower_text)
preprocessor.pipe(remove_eol_characters)
preprocessor.pipe(normalize_whitespace)
preprocessor.pipe(remove_multiple_spaces_and_strip_text)
preprocessor.pipe(remove_punct)
preprocessor.pipe(replace_currency_symbols)
preprocessor.pipe(filter_non_latin_characters)



import streamlit as st

# set page config
st.set_page_config(
	page_title="Analysez le comportement suicidaire",
	page_icon="🌄"
)

# load model on first launch
@st.cache(allow_output_mutation=True)
def load_model():
	filepath =(r"C:\Users\mateo\Desktop\TERAPP\TER-20220411T075548Z-001\TER\content\saved_model\my_model")
	# load model
	model = tf.keras.models.load_model(filepath)
	return model
# load model
with st.spinner("Loading our awesome AI 🤩. Please wait ..."):
	model = load_model()

import re


@st.cache
def handle_text(text):
	# predict
    liste = []
    liste.append(text)
    prediction = model.predict(liste)[0][0] 
	# return
    return prediction



# title and subtitle
st.title("📢 Prévention sucidaire à l'aide de tweet")
st.write("Prédisez si une personne est potentiellement suicidaire rien qu'en inscrivant un tweet 🛎️")

user_review = st.text_area(
	label="Tweet:",
	help="Mettez le tweet de votre choix ici."
)




	# display prediction

if user_review != "":
    
	prediction = handle_text(user_review)

	# display prediction
	st.subheader("AI travaille ...")

	# check prediction
	if prediction > 0.5:
		st.write(f"Nous sommes {round(prediction, 3)}% sûr que cette personne est suicidaire 😱")
	else:
		st.write(f"Cette personne va bien, nous en sommes {round(100-prediction, 3)}%  sûr ! 😇")
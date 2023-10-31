
# Got it, thanks!Here you go!Got them, thanks!
import streamlit as st
from streamlit_chat import message as st_message
import spacy
import nltk
import random
import base64

from goose3 import Goose

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.sum_basic import SumBasicSummarizer


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(jpg_file):
    bin_str = get_base64(jpg_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


set_background('background.jpg')

# st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: red;'> Simple Chatbot about ChatGPT </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: blue;'> Using spaCy library </h2>", unsafe_allow_html=True)

g = Goose()
url = 'https://en.wikipedia.org/wiki/ChatGPT'
article = g.extract(url)

# article.title

# article.cleaned_text

nltk.download('punkt')

nlp = spacy.load(r'C:\Users\Aditya\PycharmProjects\JarvisAI\en_core_web_lg-3.7.0-py3-none-any.whl')


# nlp = en_core_web_sm.load()
def preprocessing(sentence):
    # a A
    sentence = sentence.lower()
    sentence = sentence.replace('.', '')
    tokens = []
    tokens = [token.text for token in nlp(sentence) if
              not (token.is_stop or token.like_num or token.is_punct or token.is_space or len(token) == 1)]
    tokens = ' '.join([element for element in tokens])

    return tokens


original_sentences = [sentence for sentence in nltk.sent_tokenize(article.cleaned_text)]

parser = PlaintextParser.from_string(article.cleaned_text, Tokenizer('english'))

summarizer = SumBasicSummarizer()
summary = summarizer(parser.document, 10)

best_sentences = []
for sentence in summary:
    best_sentences.append(str(sentence))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def answer(user_text, threshold=0.3):
    cleaned_sentences = []
    for sentence in original_sentences:
        cleaned_sentences.append(preprocessing(sentence))
    chatbot_answer = ''
    user_text = preprocessing(user_text)
    cleaned_sentences.append(user_text)
    # print(cleaned_sentences[-1])

    tfidf = TfidfVectorizer()
    X_sentences = tfidf.fit_transform(cleaned_sentences)
    # print(X_sentences.toarray()[-1])
    similarity = cosine_similarity(X_sentences[-1], X_sentences)
    # print(similarity)
    sentence_index = similarity.argsort()[0][-2]
    # print(sentence_index)
    # print(similarity[0][sentence_index])

    if similarity[0][sentence_index] < threshold:
        chatbot_answer += 'Sorry, no answer was found!'
    else:
        chatbot_answer += original_sentences[sentence_index]

    return chatbot_answer


reply_dict = {'Who are you?': 'I am a chatbot and I will answer your questions about ChatGPT ',
              'Hey': 'Hi there! Tell me how can I assist you ', 'Hello': 'Hello, how may I assist you?',
              'Hi': 'Hey! How can I help you?', 'How can you help me?': 'I can assist you with questions on chatGPT',
              'who are you?': 'I am a chatbot and I will answer your questions about ChatGPT ',
              'hey': 'Hi there! Tell me how can I assist you ', 'hello': 'Hello, how may I assist you?',
              'hi': 'Hey! How can I help you?', 'how can you help me?': 'I can assist you with questions on chatGPT',
              'what is your source of information': 'Its Wikipedia'}
goodbye_output = ("See you later!", "Have a nice day!", "Bye! Come back again")

# history =[{"message":"user message","is_user": False},
#           {"message" :'Hello! I am a chatbot and I will answer your questions about ChatGPT',
#            'is_user' : True
#            }]

if "history" not in st.session_state:
    st.session_state.history = [
        {"message": 'Hello! I am a chatbot and I will answer your questions about ChatGPT',
         'is_user': True
         }]


# message('Hello! I am a chatbot and I will answer your questions about ChatGPT',is_user=True)

# msg_history=[]
def generate_answer():
    # i=0
    user_text = st.session_state.input_text
    if user_text != 'quit':
        if user_text in reply_dict:
            st.session_state.history.append({"message": user_text, "is_user": False})
            st.session_state.history.append({"message": reply_dict[user_text], "is_user": True})
        else:
            st.session_state.history.append({"message": user_text, "is_user": False})
            st.session_state.history.append({"message": answer(user_text), "is_user": True})

    else:
        st.session_state.history.append({"message": user_text, "is_user": False})
        st.session_state.history.append({"message": random.choice(goodbye_output), "is_user": True})


st.text_input("Type your message to the bot here", key="input_text", on_change=generate_answer)

# print("HISTORY", st.session_state.history)
for chat in st.session_state.history:
    print("CHAT", chat)
    st_message(**chat)  # unpacking
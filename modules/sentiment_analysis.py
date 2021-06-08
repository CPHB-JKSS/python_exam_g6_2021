# Imports
from nltk.tokenize import sent_tokenize
from modules import Afinn
from modules import data_preparation as dp

# vi benytter afinn til at vurdere hvorvidt en sætning / tale er postitiv eller negativ. afinn giver en score mellem -5 (negativ) og +5 (positiv).
afinn = Afinn(language='da')


def compile_data(data_dict):

    graded_dict = {}
    for speech in data_dict.items():
        print(speech[0], "=", grade_speech_sentences_sentiment(speech[1]))
        graded_dict[speech[0]] = grade_speech_sentences_sentiment(speech[1])

    return graded_dict


def grade_speech_sentiment(speech):
    # vi 'sentence-tokenizer' talen, så vi får den opdelt i sætninger.
    sentences = sent_tokenize(speech)

    count = 0
    accu_score = 0

    for sentence in sentences:
        count = count + 1
        accu_score += afinn.score(sentence)
        # print(afinn.score(sentence))

    # returnerer den gennemsnitlige 'sentiment-score' for talen
    return accu_score/count


def grade_speech_sentences_sentiment(speech):

    # vi 'sentence-tokenizer' talen, så vi får den opdelt i sætninger.
    sentences = sent_tokenize(speech)

    count = 0
    accu_score = 0
    score_dict = {}

    for sentence in sentences:

        #sentence = dp.clean_speech(sentence)

        count = count + 1
        score = afinn.score(sentence)
        accu_score += score
        score_dict[count] = score
        # print(afinn.score(sentence))
    score_dict["avg"] = accu_score/count
    # returnerer den gennemsnitlige 'sentiment-score' for talen
    return score_dict

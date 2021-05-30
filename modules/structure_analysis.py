import matplotlib.pyplot as plt
from wordcloud import WordCloud
from modules import data_preparation as dp

def top_words_all(amount,data_dtm):
    top_dict = {}
    data = data_dtm.transpose()
    for year in data.columns:
        top = data[year].sort_values(ascending=False).head(amount)
        top_dict[year] = list(zip(top.index, top.values))

    return top_dict

def top_words_by_year(search_year, amount, data_dtm):
    top_dict = {}
    data = data_dtm.transpose()
    for x in data.columns:
        if search_year == int(x):
            top = data[x].sort_values(ascending=False).head(amount)
            top_dict[x] = list(zip(top.index, top.values))
            break

    return top_dict

def create_wordcloud_format(stopwords):
    wc = WordCloud (stopwords=stopwords, background_color="white", colormap="Dark2", 
    max_font_size=150, random_state=42)
    
    return wc

def create_wordcloud_all(wc,data_dict):
    plt.rcParams['figure.figsize'] = [16,6]

    all_years = dp.get_years()

    for i, x in enumerate(data_dict.values()):
        wc.generate(x)
  

        plt.subplot(4, 5, i+1)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.title("nytårstalen " + str(all_years[i]))

    plt.show()
    
def create_wordcloud(year,wc,data_dict):
    plt.rcParams['figure.figsize'] = [16,6]
    
    text = data_dict[str(year)]
    wc.generate(text)
    
    plt.subplot()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title("nytårstalen " + str(year))
    

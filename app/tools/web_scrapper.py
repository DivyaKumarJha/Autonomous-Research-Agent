from newspaper import Article

def scrape_article(url):

    try:

        article = Article(url)

        article.download()
        article.parse()

        text = article.text

        return text

    except:

        return ""
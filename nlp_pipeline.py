# NLP pipeline for SomKaydAI

def clean_text(text):
    """
    Function nadiifiya qoraalka user-ka.
    Waxay ka saartaa meelaha bannaan, lowercase, iwm.
    """
    if not text:
        return ""

    text = text.strip()
    text = text.lower()
    return text


def preprocess(text):
    """
    Function-ka diyaariya qoraalka ka hor inta uusan engine-ku shaqeyn.
    """
    cleaned = clean_text(text)
    return cleaned

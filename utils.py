# Utility functions for SomKaydAI

def format_response(text):
    """
    Function hagaajiya jawaabta ka hor inta aan loo dirin user-ka.
    """
    if not text:
        return ""

    # Capitalize letter-ka ugu horeeya
    return text.strip().capitalize()


def is_valid_input(text):
    """
    Function hubiya in user-ku qoray wax sax ah.
    """
    if not text or not text.strip():
        return False
    return True

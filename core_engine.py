# Core engine for SomKaydAI

class SomKaydAIEngine:
    def __init__(self):
        # Meesha model-ka ama logic-ka la load-gareyn doono
        self.name = "SomKaydAI"

    def generate_response(self, user_input):
        """
        Function-ka ugu weyn ee soo saaraya jawaabaha.
        Hadda waa placeholder — laakiin waa shaqeynayaa.
        """
        if not user_input.strip():
            return "Fadlan qor wax aan ka jawaabo."

        # Placeholder response
        return f"Waxaan helay: {user_input}"

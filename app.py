# SomKaydAI main application

from core_engine import SomKaydAIEngine
from nlp_pipeline import preprocess
from utils import format_response, is_valid_input

def main():
    engine = SomKaydAIEngine()

    print("SomKaydAI Chatbot 🤖 Ready!")
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("SomKaydAI: Nabad gelyo!")
            break

        if not is_valid_input(user_input):
            print("SomKaydAI: Fadlan qor wax sax ah.")
            continue

        processed = preprocess(user_input)
        raw_response = engine.generate_response(processed)
        final_response = format_response(raw_response)

        print(f"SomKaydAI: {final_response}")

if __name__ == "__main__":
    main()

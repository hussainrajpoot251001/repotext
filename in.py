from textblob import TextBlob  
import time  

def analyze_sentiment(message):
    blob = TextBlob(message)  
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "positive"
    elif sentiment < 0:
        return "negative"
    else:
        return "neutral"

# Main Chatbot Function
def mood_analyzer_chatbot():
    print("ChatBot: Hello! Welcome to the Mood Analyzer ChatBot.")
    print("ChatBot: Share your thoughts, and I'll try to understand how you're feeling!")
    print("ChatBot: Type 'exit' anytime to end our conversation.\n")
    
    while True:
        user_message = input("You: ")
        if user_message.lower() == "exit":
            print("ChatBot: Goodbye! Stay positive and take care!")
            break
        
        # Analyze sentiment and respond accordingly
        try:
            sentiment = analyze_sentiment(user_message)
            time.sleep(1)  # Adding a delay to simulate a real chat experience
            
            if sentiment == "positive":
                print("ChatBot: That's wonderful! Keep smiling! 😊")
            elif sentiment == "negative":
                print("ChatBot: I'm sorry to hear that. Sending you positive vibes! 🌟")
            elif sentiment == "neutral":
                print("ChatBot: Got it! Thanks for sharing.")
        except Exception as e:
            print("ChatBot: Oops! I ran into an error. Please try again later.")
            print(f"Error details: {e}")
mood_analyzer_chatbot()

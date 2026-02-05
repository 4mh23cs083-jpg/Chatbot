from ai import get_ai_response
print("Welcome to the chatbot!")
print("Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    ai_response = get_ai_response(user_input)
    print(f"AI: {ai_response}")



#from flask import  Flask
#app = Flask(__name__)
#@app.route('/')
#def index():
#    return 'Hello World!'
#if __name__ == '__main__':
#    app.run(debug=True)
 
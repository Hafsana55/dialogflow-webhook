# See https://github.com/dialogflow/dialogflow-python-client-v2
# for Dialogflow fulfillment library docs, samples, and to report issues
from flask import Flask, request, jsonify
from dialogflow_fulfillment import WebhookClient, Card, Suggestion

# Initialize Flask app
app = Flask(__name__)

# Webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the incoming request from Dialogflow
    req = request.get_json(silent=True, force=True)
    print('Request Headers:', request.headers)
    print('Request Body:', req)
    
    # Create a WebhookClient instance
    agent = WebhookClient(request=req)

    # Define intent handlers
    def welcome(agent):
        agent.add("Welcome to my agent!")

    def fallback(agent):
        agent.add("I didn't understand")
        agent.add("I'm sorry, can you try again?")

    # Example custom intent handler
    def custom_handler(agent):
        agent.add("This is a custom intent response.")
        agent.add(Card(
            title="This is a card title",
            image_uri="https://developers.google.com/actions/images/badges/XPM_BADGING_GoogleAssistant_VER.png",
            subtitle="This is the body text of the card.",
            buttons=[{
                "text": "This is a button",
                "postback": "https://assistant.google.com/"
            }]
        ))
        agent.add(Suggestion("Quick Reply"))
        agent.add(Suggestion("Another Suggestion"))

    # Map intents to their respective handlers
    intent_map = {
        'Default Welcome Intent': welcome,
        'Default Fallback Intent': fallback,
        'Custom Intent': custom_handler,  # Replace with your intent name
    }

    # Handle the request based on the matched intent
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName')
    if intent in intent_map:
        intent_map[intent](agent)
    else:
        agent.add("Intent not handled!")

    # Return the response back to Dialogflow
    return agent.response()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)# See https://github.com/dialogflow/dialogflow-python-client-v2
# for Dialogflow fulfillment library docs, samples, and to report issues
from flask import Flask, request, jsonify
from dialogflow_fulfillment import WebhookClient, Card, Suggestion

# Initialize Flask app
app = Flask(__name__)

# Webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the incoming request from Dialogflow
    req = request.get_json(silent=True, force=True)
    print('Request Headers:', request.headers)
    print('Request Body:', req)
    
    # Create a WebhookClient instance
    agent = WebhookClient(request=req)

    # Define intent handlers
    def welcome(agent):
        agent.add("Welcome to my agent!")

    def fallback(agent):
        agent.add("I didn't understand")
        agent.add("I'm sorry, can you try again?")

    # Example custom intent handler
    def custom_handler(agent):
        agent.add("This is a custom intent response.")
        agent.add(Card(
            title="This is a card title",
            image_uri="https://developers.google.com/actions/images/badges/XPM_BADGING_GoogleAssistant_VER.png",
            subtitle="This is the body text of the card.",
            buttons=[{
                "text": "This is a button",
                "postback": "https://assistant.google.com/"
            }]
        ))
        agent.add(Suggestion("Quick Reply"))
        agent.add(Suggestion("Another Suggestion"))

    # Map intents to their respective handlers
    intent_map = {
        'Default Welcome Intent': welcome,
        'Default Fallback Intent': fallback,
        'Custom Intent': custom_handler,  # Replace with your intent name
    }

    # Handle the request based on the matched intent
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName')
    if intent in intent_map:
        intent_map[intent](agent)
    else:
        agent.add("Intent not handled!")

    # Return the response back to Dialogflow
    return agent.response()

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)

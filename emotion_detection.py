import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        
        # Extract the required emotions and their scores
        emotions = result.get('emotion_predictions', {}).get('document', {}).get('emotion', {})
        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)

        # Find the dominant emotion
        emotion_scores = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Return the formatted output
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    else:
        return f"Error: {response.status_code}, {response.text}"

# Sample usage:
if __name__ == "__main__":
    print(emotion_detector("I am so happy I am doing this."))

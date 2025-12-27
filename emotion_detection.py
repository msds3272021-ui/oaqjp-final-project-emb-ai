import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    response = requests.post(url, json=myobj, headers=header)
    print("Status code:", response.status_code)
    
    if response.status_code != 200:
        print("API call failed:", response.text)
        return {}
    
    response_dict = response.json()
    print(json.dumps(response_dict, indent=2))
    
    emotion_predictions = response_dict.get('emotionPredictions', [])
    print("emotion_predictions:", emotion_predictions)
    
    if not emotion_predictions:
        print("No emotionPredictions found in response.")
        return {}
    
    emotions_data = emotion_predictions[0].get('emotion', None)
    print("emotions_data:", emotions_data)
    
    if emotions_data is None or len(emotions_data) == 0:
        print("No emotion data found inside emotionPredictions[0].")
        return {}
    
    anger_score = float(emotions_data.get('anger', 0))
    disgust_score = float(emotions_data.get('disgust', 0))
    fear_score = float(emotions_data.get('fear', 0))
    joy_score = float(emotions_data.get('joy', 0))
    sadness_score = float(emotions_data.get('sadness', 0))
    
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant_emotion'] = dominant_emotion
    
    print("Emotion scores:", emotions)
    print("Dominant emotion:", dominant_emotion)
    
    return emotions
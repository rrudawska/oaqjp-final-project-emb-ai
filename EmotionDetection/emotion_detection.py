import requests
import json


def emotion_detection(text_to_analyse):
    # Define the URL for the analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create the payload with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyse}}
    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 400:
        return {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None,
                "dominant_emotion": None}

    formatted = json.loads(response.text)
    result = formatted["emotionPredictions"][0]["emotion"]

    dominant = 0
    dominant_emotion = ""

    for emotion in result:
        if result[emotion] > dominant:
            dominant = result[emotion]
            dominant_emotion = emotion

    result["dominant_emotion"] = dominant_emotion

    return result
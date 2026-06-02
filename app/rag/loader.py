from youtube_transcript_api import YouTubeTranscriptApi


def load_youtube_transcript(video_id: str):

    ytt_api = YouTubeTranscriptApi()

    fetched = ytt_api.fetch(
        video_id, languages=["hi", "en"]
    )  

    text = " ".join([x.text for x in fetched])  

    return text

from fastapi import FastAPI

app = FastAPI()

@app.get("/info")
def get_info(topic: str):

    return {
        "topic": topic,
        "content": f"{topic} is an important concept used in real-world applications and technology.",
        "points": [
            f"Definition of {topic}",
            f"Core concepts of {topic}",
            f"How {topic} works",
            f"Real-world applications of {topic}",
            f"Advantages of {topic}",
            f"Limitations of {topic}"
        ]
    }
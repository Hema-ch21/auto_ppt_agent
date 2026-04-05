import wikipedia
from auto_ppt_agent.ppt_tools import create_ppt


def get_info(topic):

    try:
        return wikipedia.summary(topic, sentences=10)
    except:
        return f"{topic} is an important topic in modern technology used across industries."


def to_points(text):

    sentences = text.split(".")
    points = []

    for s in sentences:
        s = s.strip()
        if len(s) > 25:
            points.append(s)

    return points


# ------------------ SMART SPLIT ------------------
def split_points(points):

    n = len(points)

    return {
        "overview": points[:3],
        "concepts": points[3:6] if n > 3 else points[:3],
        "extra": points[6:9] if n > 6 else points[:3]
    }


def run(topic):

    text = get_info(topic)
    points = to_points(text)

    sections = split_points(points)

    slides = [
        {
            "title": f"{topic} - Overview",
            "points": sections["overview"],
            "image": topic
        },
        {
            "title": f"{topic} - Key Concepts",
            "points": sections["concepts"],
            "image": topic
        },
        {
            "title": f"{topic} - Applications",
            "points": sections["extra"],
            "image": topic
        },
        {
            "title": f"{topic} - Advantages",
            "points": [
                "Saves time and effort",
                "Improves accuracy",
                "Reduces manual workload"
            ],
            "image": topic
        },
        {
            "title": f"{topic} - Conclusion",
            "points": [
                f"{topic} plays a major role in modern systems",
                "It has strong real-world applications",
                "Future scope is very high"
            ],
            "image": topic
        }
    ]

    return create_ppt(slides)
from dotenv import load_dotenv
import os
import cohere

load_dotenv()

API_KEY = os.getenv("API_KEY")
co = cohere.Client(API_KEY)
text = """Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.
"""

response = co.summarize(
    text, model="summarize-xlarge", length="medium", extractiveness="high"
)

summary = response.summary

print(summary)
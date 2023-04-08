from fastapi import FastAPI
from pydantic import BaseModel
import spacy
from spacy.matcher import Matcher

app = FastAPI()
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# Define a Pydantic model for the request body
class TextInput(BaseModel):
    text: str

@app.post("/score_text")
def score_text(text_input: TextInput):
    """Endpoint to score text for uncertain statements using spaCy Matcher."""
    # Load the text into spaCy's nlp object
    doc = nlp(text_input.text)

    # Define spaCy Matcher patterns for uncertain statements
    pattern1 = [{"IS_ALPHA": True, "OP": "?"}, {"ORTH": "may"}, {"IS_ALPHA": True, "OP": "?"}]
    pattern2 = [{"IS_ALPHA": True, "OP": "?"}, {"ORTH": "might"}, {"IS_ALPHA": True, "OP": "?"}]
    pattern3 = [{"IS_ALPHA": True, "OP": "?"}, {"ORTH": "could"}, {"IS_ALPHA": True, "OP": "?"}]

    # Add the patterns to the Matcher
    matcher.add("UNCERTAIN_STATEMENT", [pattern1, pattern2, pattern3])

    # Use the Matcher to find matches in the text
    matches = matcher(doc)

    # Extract matched spans and their associated text
    uncertain_statements = [doc[start:end].text for _, start, end in matches]

    # Calculate the score as the ratio of uncertain statements to the total number of sentences
    score = len(uncertain_statements) / len(list(doc.sents))

    # Return the score
    return {"score": score, "uncertain_statements": uncertain_statements}

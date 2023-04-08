# spacy-fastapi-ceo-uncertainty

First run the server:

```
uvicorn main:app --reload
```

In a new terminal:

```
curl -X POST "http://localhost:8000/score_text" -H "accept: application/json" -H "Content-Type: application/json" -d '{
  "text": "Dear shareholders, we may face challenges in the coming quarter due to uncertain market conditions. Our revenues might be impacted by factors beyond our control, such as economic fluctuations and regulatory changes. However, we remain committed to our long-term strategy and will continue to explore new opportunities. Thank you for your continued support."
}'
```
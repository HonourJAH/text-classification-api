import joblib

data = joblib.load("model.joblib")
pipeline = data["pipeline"]
categories = data["categories"]

result1 = pipeline.predict(["The universe is vast and full of stars."])
print(f"Predicted category: {categories[result1[0]]}")
result2 = pipeline.predict(["Atheism is a belief system."])
print(f"Predicted category: {categories[result2[0]]}")
result3 = pipeline.predict(["The Earth revolves around the Sun."])
print(f"Predicted category: {categories[result3[0]]}")
result4 = pipeline.predict(
    ["The Bible and the Quran are central texts in religious practice"]
)
print(f"Predicted category: {categories[result4[0]]}")
result5 = pipeline.predict(
    ["Christians and Muslims share many common values and traditions in their worship"]
)
print(f"Predicted category: {categories[result5[0]]}")

result6 = pipeline.predict(
    ["Jesus Christ died for our sins and rose again on the third day"]
)
print(f"Predicted category: {categories[result6[0]]}")

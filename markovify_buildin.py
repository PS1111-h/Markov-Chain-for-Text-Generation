import markovify

with open("macbeth.txt", "r") as f:
    text = f.read()

# Build the Markov model
text_model = markovify.Text(text)

# Generate and print five random sentences
print("Randomly-Generated Sentences:")
for i in range(5):
    print(text_model.make_sentence())

# Generate and print three random short sentences (max 280 characters)
print("\nShort Sentences (Max 280 characters):")
for i in range(3):
    print(text_model.make_short_sentence(280))


# reference: https://github.com/jsvine/markovify/tree/master?tab=readme-ov-file
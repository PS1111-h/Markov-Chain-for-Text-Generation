import random
import re
from collections import defaultdict

#Preprocessing
def preprocess_text(file):
    content = open(file).read()  # Open the file
    cleaned_content = re.sub('[^a-zA-Z0-9\n]', ' ', content)  # Clean special characters
    cleaned_content = cleaned_content.lower()  # Convert to lowercase
    # open('CleanedText.txt', 'w').write(cleaned_content)  # Save the cleaned text to a file
    words = cleaned_content.split()  # Tokenize into words
    return words

#Transition Model
def transition_model(words, n=1):
    transition_counts = defaultdict(lambda: defaultdict(int))#use lambda in case of unknown key    
    for i in range(len(words) - n):
        key = tuple(words[i:i + n])  # Create n-gram key
        next_word = words[i + n]  # Get the next word
        transition_counts[key][next_word] += 1  # increment count for the transition

    transition_model = {}
    for key, next_words in transition_counts.items():
        total = sum(next_words.values())  # Total count of all transitions
        transition_model[key] = {word: count / total for word, count in next_words.items()}  # Normalize
    
    return transition_model

#Generate Text
def generate_text(transition_model, length, n=1):
    key = random.choice(list(transition_model.keys()))  # Randomly select a starting n-gram
    result = list(key)  # Initialize the result

    for _ in range(length - n):  # Generate the remaining words
        next_words = transition_model.get(key)
        if not next_words:  # If no next words exist, stop generation
            break
        next_word = random.choices(list(next_words.keys()), weights=next_words.values())[0]# Use transition probabilities to pick the next word
        result.append(next_word)  # Add the next word to the result
        key = tuple(result[-n:])  # Update the current n-gram

    return ' '.join(result)

# Main Execution
if __name__ == "__main__":
    # Preprocess the text file
    words = preprocess_text('macbeth.txt')
    n = 2  # bigram to improve coherence
    transition_model = transition_model(words, n)
    
    # Generate and print four text samples
    for i in range(4):
        print(f"Generated Text Sample {i + 1}:")
        print(generate_text(transition_model, length=30, n=n))
        print("\n" + "-" * 50 + "\n")

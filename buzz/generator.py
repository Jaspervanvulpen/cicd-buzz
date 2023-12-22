from __future__ import print_function
import random

buzz = (
    'continuous testing',
    'continuous integration',
    'continuous deployment',
    'continuous improvement',
    'devops'
)

adjectives = (
    'complete',
    'modern',
    'self-service',
    'integrated',
    'end-to-end'
)

adverbs = (
    'remarkably',
    'enormously',
    'substantially',
    'significantly',
    'seriously'
)

verbs = (
    'accelerates',
    'improves',
    'enhances',
    'revamps',
    'boosts'
)

# Renamed 'l' to 'items' to avoid ambiguity
def sample(items, n=1):
    result = random.sample(items, n)
    if n == 1:
        return result[0]
    return result

def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([
        sample(adjectives),
        buzz_terms[0],
        sample(adverbs),
        sample(verbs),
        buzz_terms[1]
    ])
    return phrase.title()

# Two blank lines after the function definition
if __name__ == "__main__":
    print(generate_buzz())

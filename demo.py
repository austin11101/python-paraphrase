import warnings
from parrot.parrot import Parrot

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=FutureWarning)

# Initialize Parrot Model
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)

# Input sentence to paraphrase
phrases = ["I love coding"]

for phrase in phrases:
    print("-" * 100)
    print(phrase)
    print("-" * 100)

    para_phrases = parrot.augment(
        input_phrase=phrase,
        diversity_ranker="levenshtein",
        do_diverse=True,  # Set to True for more diverse results
        max_return_phrases=10,
        max_length=64,  # Increase max length to allow longer paraphrases
        adequacy_threshold=0.70,  # Lower from 0.99
        fluency_threshold=0.50   # Lower from 0.90
    )

    if para_phrases:
        for paraphrase in para_phrases:
            print(paraphrase)
    else:
        print("⚠️ No paraphrases generated.")

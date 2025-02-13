from parrot import Parrot
import torch

# Initialize Parrot Model
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)

# Input sentences to paraphrase
phrases = ["Can you explain this in a different way?", "How are you doing today?"]

for phrase in phrases:
    print(f"\nOriginal: {phrase}")
    paraphrases = parrot.augment(input_phrase=phrase, diversity_ranker="levenshtein", do_diverse=True)
    if paraphrases:
        for paraphrase in paraphrases:
            print(f"Paraphrased: {paraphrase}")

from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer

# Sample predictions and references
preds = ["X is a subclass of Z due to transitivity."]
refs = ["X is also a subclass of Z because it inherits from Y and Z."]

# BLEU score
bleu = sentence_bleu([refs[0].split()], preds[0].split())
print(f"BLEU score: {bleu:.4f}")

# ROUGE score
scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
scores = scorer.score(refs[0], preds[0])
print(f"ROUGE-L: {scores['rougeL'].fmeasure:.4f}")

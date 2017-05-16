# beeva-poc-automatic-question-answering
Proof of Concept with Automatic Question Answering and Question Generation

## Question Generation
Use NLP fundamentals to generate "fill the gap" questionnaires from Wikipedia pages.

NLP Tools: *Python3, NLTK, TextBlob, (Multilingual) WordNet*
Process
- Segment into sentences with TextBlob Tokenizer
- Filter sentences with simple rules
- Select a common noun per sentence with Part of Speech (PoS) Tagger
  - **English**: *TextBlob PatternParser* (Penn Treebank tagset)
  - **Spanish**: *spaghetti-tagger* (EAGLES tagset). *Note*: Pattern supports Spanish, but not python3
- Generate distractors with *WordNet*

* See https://github.com/beeva-enriqueotero/wikipedia-question-generator
* Based on https://github.com/atbaker/wikipedia-question-generator


### Old dummy version
```
python mvp.py
# Usage: python mvp.py <word_to_search_in_wikipedia> <number_of_sentences>
python mvp.py Isabel 1
# Output: This set of names is a southwestern European variant of the ... name Elisheva, also represented in English and other western languages as Elizabeth
# Missing word: Hebrew
```

## Question Answering
Test MS-Cognitive https://qnamaker.ai/: From FAQ to Bot in minutes
* Example Spanish FAQs: https://aws.amazon.com/es/ec2/faqs/

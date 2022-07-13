#!/usr/bin/env python

from natasha import (
    Segmenter,
    MorphVocab,
    
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    
    PER,
    NamesExtractor,

    Doc
)

segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)

names_extractor = NamesExtractor(morph_vocab)

def get_names(text):

 doc = Doc(text)

#segmentation
#print('SEGMENTATION')
 doc.segment(segmenter)
#print(doc.tokens[:5])
#print(doc.sents[:5])

#morph
#print('MORPHOLOGY')
 doc.tag_morph(morph_tagger)
#print(doc.tokens[:5])
#doc.sents[0].morph.print()

# lemmatization

# syntax
#print('SYNTAX')
 doc.parse_syntax(syntax_parser)
#print(doc.tokens[:5])
#doc.sents[0].syntax.print()

#ner
#print('NER')
 doc.tag_ner(ner_tagger)
#print(doc.spans[:5])
#doc.ner.print()

#ne normalization
 for span in doc.spans:
    span.normalize(morph_vocab)
#print(doc.spans[:5])
#print({_.text: _.normal for _ in doc.spans if _.text != _.normal})


 for span in doc.spans:
    if span.type == PER:
        span.extract_fact(names_extractor)

#print(doc.spans[:5])
#print({_.normal: _.fact.as_dict for _ in doc.spans if _.type == PER})
 names = {_.normal: _.fact.as_dict for _ in doc.spans if _.type == PER and hasattr(_.fact, 'as_dict')}

 return list(names.values())[0] if len(names.values()) != 0 else {}


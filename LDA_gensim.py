
import os
import logging
import gensim

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# load id->word mapping (the dictionary), one of the results of step 2 above
id2word = gensim.corpora.Dictionary.load_from_text(os.path.join('DATA', 'OUT', 'wiki_wordids.txt.bz2'))
# load corpus iterator
mm = gensim.corpora.MmCorpus(os.path.join('DATA', 'OUT', 'wiki_tfidf.mm.bz2'))

print(mm)

# Train LDA
# extract 100 LDA topics, using 1 pass and updating once every 1 chunk (10,000 documents)
lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=100, update_every=1, passes=1)

# Save LDA
lda_model = os.path.join("DATA", "OUT", "wiki_LDA")
lda.save(lda_model)

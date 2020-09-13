import nltk
import gensim
import numpy as np
#nltk.download('punkt')
from nltk.tokenize import word_tokenize, sent_tokenize

def similitud(doc1, doc2):

    file_docs = []
    with open (doc1) as f:
        tokens = sent_tokenize(f.read())
        #print(tokens,"verga",len(tokens))

        for line in tokens:
            file_docs.append(line)
            

    #print(len(file_docs),file_docs)

    gen_docs = [[w.lower() for w in word_tokenize(text)] for text in file_docs]

    #print(gen_docs)

    dictionary = gensim.corpora.Dictionary(gen_docs)

    #print(dictionary.token2id)

    corpus = [dictionary.doc2bow(gen_docs) for gen_docs in gen_docs]
    #print(corpus)

    tf_idf = gensim.models.TfidfModel(corpus) #######################
    #for doc in tf_idf[corpus]:
    #   print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])
    sims = gensim.similarities.Similarity('workdir/',tf_idf[corpus],num_features=len(dictionary))
    #sims = gensim.similarities.Similarity(tf_idf[corpus],num_features=len(dictionary))

    #print(sims)

    ######################################doc_query

    file2_doc = []
    with open(doc2) as f:
        tokons = sent_tokenize(f.read())
        for line in tokons:
            file2_doc.append(line)
    #print(file2_doc)

    for line in file2_doc:
        query_doc = [w.lower() for w in word_tokenize(line)]
        query_doc_bow = dictionary.doc2bow(query_doc) 

    query_doc_tf_idf = tf_idf[query_doc_bow]
    #print(sims[query_doc_tf_idf])
    res = (max(sims[query_doc_tf_idf])*100)/len(file_docs)
    return res
    #print(uno,"se parecen a",dos,"en un" , res)


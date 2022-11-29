from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'E:\Downloads\stanford-corenlp-4.5.1')

print (nlp.parse('Tell me the number of students in EC601 on Wednesday.'))
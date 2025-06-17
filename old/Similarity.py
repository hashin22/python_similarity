'''
doc1 = "The fat cat sat on the mat"
doc2 = "The lovely dog slept on the table"

doc1_tokenized = doc1.split()
doc2_tokenized = doc2.split()


#print(f"doc1 토큰화 결과: {doc1_tokenized}")
#print(f"doc2 토큰화 결과: {doc2_tokenized}")


#doc1 토큰화 결과: ['The', 'fat', 'cat', 'sat', 'on', 'the', 'mat']
#doc2 토큰화 결과: ['The', 'lovely', 'dog', 'slept', 'on', 'the', 'table']


doc_union = set(doc1_tokenized).union(set(doc2_tokenized))


print(f"합집합 결과: {doc_union}")


doc_intersection = set(doc1_tokenized).intersection(set(doc2_tokenized))


print(f"교집합 결과: {doc_intersection}")


jaccard_similarity = len(doc_intersection) / len(doc_union)
print(f"자카드 유사도: {jaccard_similarity:.2f}")

'''

# from konlpy.tag immport Okt

# okt = Okt()

# text = "안녕하세요 파이썬"
# nouns = okt.nouns(text)
# print(nouns)
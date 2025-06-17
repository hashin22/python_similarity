'''

import pandas as pd

def jaccard_similarity(text1, text2):
    set1 = set(str(text1).split())
    set2 = set(str(text2).split())
    union = set1.union(set2)
    intersection = set1.intersection(set2)

    if len(union) == 0:
        return 0.0
    return round(len(intersection) / len(union),4)

# 엑셀파일 불러오기
doc1_df = pd.read_excel('data\\TOBE_제품확대.xlsx')
doc2_df = pd.read_excel('data\\발화데이터_ASIS.xlsx')

# 결과 저장 리스트
results = []

# 모든 문장 비교 후 유사도 계산
for i in range(len(doc1_df)) :
    text1 = doc1_df.iloc[i, 0] # 첫번째 파일 문장
    max_similarity = 0
    best_match = ""
    for j in range(len(doc2_df)):
        text2 = doc2_df.iloc[j, 0] #두번째 파일 문장
        similarity = jaccard_similarity(text1, text2)
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = text2
    results.append({
        '문장1': text1,
        '최고 매칭문장' : best_match,
        '유사도' : max_similarity
    })

# 결과를 데이터프레임으로 변환
result_df = pd.DataFrame(results)

# 엑셀로 저장
result_df.to_excel('result\\similarity.xlsx', index=False)
print("최고 유사도 계산 완료 및 저장")

'''
# H-Index
def solution(citations):
    citations = sorted(citations, reverse=True)
    for i, citation in enumerate(citations):
        if i + 1 > citation:
            return i
    return len(citations)

def solution(today, terms, privacies):

    today = list(map(int, today.split('.')))
    today = (today[0] - 2000) * 336 + today[1] * 28 + today[2]
    dict_terms = dict()
    for term in terms:
        term = term.split()
        dict_terms[term[0]] = int(term[1])

    answer = []

    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        date = list(map(int, date.split('.')))
        date = (date[0] - 2000) * 336 + date[1] * 28 + date[2]
        youhyo = date + dict_terms[term] * 28
        if youhyo <= today:
            answer.append(i + 1)

    return answer

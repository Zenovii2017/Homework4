def all_prefixes(sentence):
    sentences = set()
    while sentence[0] == ' ':
        sentence = sentence[1:]
    for j in range(len(sentence)):
        if sentence[j] == sentence[0]:
            for i in range(j, len(sentence)):
                sentences.add(sentence[j:i + 1])
    return sentences



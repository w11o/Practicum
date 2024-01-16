import pickle
def stat(file_name: str) -> dict:
    with open(file_name) as f:
        a = [i.strip(',.!?-') for i in f.readline().split()]
        res = {}
        for i in a:
            res[i] = res.get(i, 0) + 1
        return res

f = open('pickle_stat_1', 'wb')
pickle.dump(stat('stat1'), f)
f.close()

f = open('pickle_stat_2', 'wb')
pickle.dump(stat('stat2'), f)
f.close()

f = open('pickle_stat_3', 'wb')
pickle.dump(stat('stat3'), f)
f.close()



f = open('pickle_stat_1', 'rb')
load1 = pickle.load(f)
f.close()

f = open('pickle_stat_2', 'rb')
load2 = pickle.load(f)
f.close()

f = open('pickle_stat_3', 'rb')
load3 = pickle.load(f)
f.close()


def word_counts(dict1, dict2):
    merged_dict = dict1.copy()
    for word, count in dict2.items():
        if word in merged_dict:
            merged_dict[word] += count
        else:
            merged_dict[word] = count
    return merged_dict


res = word_counts(load1,load2)
res = word_counts(res, load3)
print(res)

with open('result.txt', 'w') as f:
    for word, count in res.items():
        f.write(f'Word "{word}" was {count} times in text' + '\n')




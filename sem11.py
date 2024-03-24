#1
# import csv
#
# def stat(file_name, words=100):
#     statistic = {}
#     words_list = []
#     res=[]
#
#     def srt(arg):
#         return arg[1]
#
#     with open(file_name, 'r', encoding='utf-8') as f:
#         for c in list(f):
#             for j in c.split():
#                 words_list.append(j.strip('\n!.?,'))
#
#         if type(words) == int:
#             for i in words_list[:words]:
#                 statistic[i] = statistic.get(i, 0) + 1
#
#             for i in statistic.items():
#                 res.append(i)
#             print(*sorted(res, key=srt, reverse=True), sep='\n')
#
#
#         if type(words) == float:
#             for i in words_list[:100]:
#                 statistic[i] = statistic.get(i, 0) + 1
#
#             for i in statistic.items():
#                 res.append(i)
#
#             with open(str(words), 'w', newline='') as csvfile:
#                 writer = csv.writer(csvfile)
#                 writer.writerows(res)
#
# stat('stat', 20)



# 2
# import csv
#
# def stat():
#     statistic = {}
#     words_list = []
#     res=[]
#     file_name = None
#
#     def srt(arg):
#         return arg[1]
#
#
#     while True:
#         file_name = input()
#         if file_name == '':
#             break
#         with open(file_name, 'r', encoding='utf-8') as f:
#             for c in list(f):
#                 for j in c.split():
#                     words_list.append(j.strip('\n!.?,'))
#
#         for i in words_list[:100]:
#             statistic[i] = statistic.get(i, 0) + 1
#
#         for i in statistic.items():
#             res.append(i)
#
#     print('Введите имя создоваемого файла:')
#     with open(str(input()), 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerows(res)
#
# stat()



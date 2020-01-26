import pandas as pd

print("====== Data Frames =====")
list_1 = [1, 2, 3, 4, 5]
data_frame_1 = pd.DataFrame(list_1)
print("data_frame_1: {}".format(data_frame_1))

map_1 = {'fruit': ['apple', 'orange', 'mango'], 'count': [10, 20, 15]}
data_frame_2 = pd.DataFrame(map_1)
print("data_frame_1:\n{}".format(data_frame_2))

table_1 = pd.read_csv("pandas-test-1.csv")
print("table_1 csv:\n{}".format(table_1))

print("table_1 csv head:\n{}".format(table_1.head()))

print("===== length of words in a list =======")
series_1 = pd.Series(["marry", "had", "a", "little", "lamb"])
print("series_1:\n{}".format(series_1))

series_1_word_cnt = series_1.map(lambda a: len(a))
print("series_1 word count:\n{}".format(series_1_word_cnt))






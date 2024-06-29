import pickle

# 定义一个函数来获取词汇表
def get_vocab(corpus1, corpus2):
    word_vocab = set()  # 初始化一个空集合来存储词汇
    for corpus in [corpus1, corpus2]:  # 对每个语料库进行遍历
        for i in range(len(corpus)):  # 对语料库中的每个元素进行遍历
            # 更新词汇集合，添加新的词汇
            word_vocab.update(corpus[i][1][0])
            word_vocab.update(corpus[i][1][1])
            word_vocab.update(corpus[i][2][0])
            word_vocab.update(corpus[i][3])
    print(len(word_vocab))  # 打印词汇集合的大小
    return word_vocab  # 返回词汇集合

# 定义一个函数来加载pickle文件
def load_pickle(filename):
    with open(filename, 'rb') as f:  # 打开文件
        data = pickle.load(f)  # 加载文件
    return data  # 返回加载的数据

# 定义一个函数来处理词汇
def vocab_processing(filepath1, filepath2, save_path):
    with open(filepath1, 'r') as f:  # 打开文件
        total_data1 = set(eval(f.read()))  # 读取文件内容，并将其转化为集合
    with open(filepath2, 'r') as f:  # 打开文件
        total_data2 = eval(f.read())  # 读取文件内容

    word_set = get_vocab(total_data2, total_data2)  # 获取词汇表

    # 找出需要排除的词汇
    excluded_words = total_data1.intersection(word_set)
    word_set = word_set - excluded_words  # 从词汇表中排除这些词汇

    print(len(total_data1))  # 打印总数据1的长度
    print(len(word_set))  # 打印词汇表的长度

    with open(save_path, 'w') as f:  # 打开文件
        f.write(str(word_set))  # 将词汇表写入文件

# 主函数
if __name__ == "__main__":
    python_hnn = './data/python_hnn_data_teacher.txt'
    python_staqc = './data/staqc/python_staqc_data.txt'
    python_word_dict = './data/word_dict/python_word_vocab_dict.txt'

    sql_hnn = './

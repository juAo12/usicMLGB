""" Convert libsvm data from AFN paper to csv format """
import pandas as pd
from pathlib import Path
import gc
import hashlib
import tqdm

headers = ["label", "I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10",
           "I11", "I12", "I13", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10",
           "C11", "C12", "C13", "C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22",
           "C23", "C24", "C25", "C26"]

data_files = ["./criteo/train.libsvm", "./criteo/valid.libsvm", "./criteo/test.libsvm"]
#
# for f in data_files:
#     print("reading file: " + f)
#     df = pd.read_csv(f, sep=" ", names=headers)
#     print("reading success")
#     # for col in headers[1:]:
#     for col in tqdm.tqdm(headers[1:]):
#         if col.startswith("I"):
#             df[col] = df[col].apply(lambda x: x.split(':')[-1])
#         elif col.startswith("C"):
#             df[col] = df[col].apply(lambda x: x.split(':')[0])
#     df.to_csv(Path(f).stem + ".csv", index=False)
#     del df
#     gc.collect()


chunk_size = 5000000  # 可以根据你的内存大小调整这个值
for f in data_files:
    print("Reading file: " + f)

    # 使用 chunksize 逐块读取文件
    chunks = pd.read_csv(f, sep=" ", names=headers, chunksize=chunk_size)

    for chunk in chunks:
        # 处理每个数据块
        for col in tqdm.tqdm(headers[1:]):
            if col.startswith("I"):
                chunk[col] = chunk[col].apply(lambda x: x.split(':')[-1] if isinstance(x, str) else x)
            elif col.startswith("C"):
                chunk[col] = chunk[col].apply(lambda x: x.split(':')[0] if isinstance(x, str) else x)
    print("Reading success")

    # 清理内存
    del chunks
    gc.collect()

# Check md5sum for correctness
assert("30b89c1c7213013b92df52ec44f52dc5" == hashlib.md5(open('train.csv', 'r').read().encode('utf-8')).hexdigest())
assert("f73c71fb3c4f66b6ebdfa032646bea72" == hashlib.md5(open('valid.csv', 'r').read().encode('utf-8')).hexdigest())
assert("2c48b26e84c04a69b948082edae46f8c" == hashlib.md5(open('test.csv', 'r').read().encode('utf-8')).hexdigest())

print("Reproducing data succeeded!")
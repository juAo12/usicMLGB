# import tensorflow as tf
#
#
# def normalize_date(date):
#     date = str(date)
#     print(date)
#     # print(len(date))
#
#     if len(date) == 8:
#         return date[:4] + '-' + date[4:6] + '-' + date[6:]
#     elif len(date) == 17:  # ex: 20240301_20240307, 拿后缀
#         x = date[-8:-4] + '-' + date[-4:-2] + '-' + date[-2:]
#         print('ok')
#         return x
#     return date
#
# if __name__ == '__main__':
#     date = normalize_date(20240613_20240613)
#     # date = normalize_date(20240613)
#     # print(date)
#
#
# # def list_dirs_by_date_range(root_path, begin_date, end_date):
# #     begin_date = normalize_date(begin_date)
# #     end_date = normalize_date(end_date)
# #     root = root_path if root_path[-1] == '/' else root_path + '/'
# #     dates = filter(lambda d: begin_date <= normalize_date(d) <= end_date, tf.gfile.ListDirectory(root_path))
# #     return [root + d + '/' for d in dates]
# #
# #
# # def list_files_by_date_range(root_path, begin_date, end_date):
# #     files = []
# #     for d in list_dirs_by_date_range(root_path, begin_date, end_date):
# #         paths = tf.gfile.ListDirectory(d)
# #         if 'out_gr_record_train' in paths:
# #             d = d + 'out_gr_record_train/'
# #             paths = tf.gfile.ListDirectory(d)
# #         for p in paths:
# #             files.append(d + p)
# #     print(sorted(files))
# #     return sorted(files)
# #
# #
# # data_path = '/user/ca_alg/data/zrec/models/app_web_click_ocpc/rank_dataset/train_data/group_daily/'
# # data_path2 = '/user/ca_alg/data/zrec/models/effect_ocpc_new/nn/rank_dataset/features/train_data/'
# # dates = [20240608, 20240613]
# # match_files = list_files_by_date_range(data_path, dates[0], dates[1])




date = 20240613_20240613
print
date = str(date)
print(date)
import tensorflow as tf
import numpy as np
import pre_for_work

def data_init():
    korea_data = pre_for_work.South_Korea_DataSet()
    china_data = pre_for_work.China_DataSet()
    return korea_data,china_data


if "__main__"==__name__:
    korea_data_set,china_data_set=data_init()
    detail_list=[]
    site_list=[]
    for data in korea_data_set.data_set.data_list:
        if data.site not in site_list:
            site_list.append(data.site)
        if data.detail_site not in detail_list:
            detail_list.append(data.detail_site)
    print(detail_list)
    print(site_list)
    print(len(detail_list))
    print(len(site_list))







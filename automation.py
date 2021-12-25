import auto_record
import config
import predict

if __name__ == '__main__':
    for i in range(config.TEST_TIMES):
        file_name = "file_test" + str(i) + ".mp4"
        auto_record.record_task(file_name)
    result_list = []

    for i in range(config.TEST_TIMES):
        file_name = "./video/file_test" + str(i) + ".mp4"
        result_list.append(predict.predict(file_name))

    print(result_list)

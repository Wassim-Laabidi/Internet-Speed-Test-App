import speedtest


def get_result():
    test = speedtest.Speedtest()
    download_result = test.download() / 1024 / 1024
    upload_result = test.upload() / 1024 / 1024
    ping_result = test.results.ping
    download_result = round(download_result, 2)
    upload_result = round(upload_result, 2)
    result = {"download_result": str(download_result)+" Mbit/s", "upload_result": str(upload_result)+" Mbit/s",
              "ping_result": str(ping_result)+" Mbit/s"}
    return result

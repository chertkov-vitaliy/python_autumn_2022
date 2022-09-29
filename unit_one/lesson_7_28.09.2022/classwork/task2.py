#todo: задан словарь



# Нужно создать  файл config.txt с содержимым вида:
sdtv_mode=2
hdmi_drive=2
hdmi_group=2
hdmi_mode=16
overscan_left=20
overscan_right=12
overscan_top=10


FILE = "config.txt"
settings = { "sdtv_mode":2, "hdmi_drive":2, "hdmi_group":2, "hdmi_mode":16, "overscan_left":20, "overscan_right":12, "overscan_top":10 }

def create_file():
    fd = open(FILE, mode="at")
    for key, value in settings.items():
        fd.write(key + "=" + str(value) + "\n")
    fd.close()

create_file()







import re
import os
import pickle

from administer_data.scraping.softbank.sb_scrape_class_info import SBscraping as sb
from administer_data import models
# from administer_data.scraping.data import softbank_data as sb_data


def save_data_to_pkl_file(data: dict, file_path):
    with open(
            os.path.join("./administer_data/scraping/data/softbank/",
                         file_path + ".pkl"), 'wb') as f:
        pickle.dump(data, f)


def load_data_from_pkl_file(file_path) -> dict:
    with open(
            os.path.join('./administer_data/scraping/data/softbank/',
                         file_path + ".pkl"), 'rb') as f:
        dict_pkl = pickle.load(f)
    return dict_pkl


def save_fixed_data_to_model(src_file="softbank_test"):
    """ 
    pklファイルに保存されたデータからインスタンスを作成しモデルに保存する関数
    scrapingする関数の呼び出しや情報のUPDATEとかもできたらいいなと思っている
    """
    data = load_data_from_pkl_file(file_path=src_file)
    # area = (pref_id, area_id), area_name(店舗数))
    # class_info_xs = {
    # "店舗名": {
    #     'phone_number':
    #     'class_name':
    #     'has_parking':
    #     'is_barrier_free':
    #     'address':
    # }

    city_name_pattern = re.compile(r'[^0-9（）]+')

    org, _ = models.ClassOrganizer.objects.get_or_create(
        organizer_name="ソフトバンク")
    pref = models.Prefecture.objects.get(pref_name="東京都")

    for area, class_info_xs in data.items():
        if not class_info_xs:
            continue

        city_name = city_name_pattern.match(area[1]).group()
        city, _ = models.City.objects.get_or_create(city_name=city_name,
                                                    prefecture=pref)

        for class_info in class_info_xs.values():
            class_info = models.ClassInfo.objects.create(city=city,
                                                         class_organizer=org,
                                                         **class_info)

    # print(models.City.objects.all())
    sb.quit_driver()


# def dict_to_pkl_file():
#     # print(sb_data.data)

#     sb.save_data_file_pkl(sb_data.data, "softbank-2022_11_26_14_50_49")
#     # sb.save_data_file_pkl(sb_data.data, "softbank_test")


def fix_data(src_file="softbank_test"):
    data = load_data_from_pkl_file(src_file)
    # print(data)
    for area, class_info_xs in data.items():
        for class_info in class_info_xs.values():
            if class_info["has_parking"] in ["None", "－"]:
                class_info["has_parking"] = False
            else:
                class_info["has_parking"] = True

            if class_info["is_barrier_free"] == "－":
                class_info["is_barrier_free"] = False
            else:
                class_info["is_barrier_free"] = True

    # print(data)
    sb.save_data_file_pkl(data, file_path=src_file + "_fixed")
    sb.quit_driver()
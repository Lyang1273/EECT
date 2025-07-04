import requests
import json
import tomllib
import traceback
from loguru import logger
import maliang

config_path = "./config/LibConfig.toml"
language_path = "./config/Language.toml"


with open(config_path, "rb") as f:
    lib_config = tomllib.load(f)


def lib_version():
    return 2, 250701.1    # 版本， build号


# noinspection PyMethodMayBeStatic
class EggHunt:
    def EggHuntLoad(self):
        logger.info("加载彩蛋信息")
        with open("./config/config.toml", "rb") as f:
            EggHuntConfig = tomllib.load(f)

            egg_hunt = EggHuntConfig["EggHunt"]

    def LyangThirteenYearsOld(self):
        logger.info("触发彩蛋：LyangThirteenYearsOld")
        print("哇咔咔，EECT13篡位！！！\n7月3日是开发者Lyang的生日呀，生日快乐~")


# noinspection PyMethodMayBeStatic
class Weather:
    def get_weather(self, city):
        weather_data = requests.get(f"https://api.52vmy.cn/api/query/tian?city={city}").json()
        # 解析JSON数据
        try:
            # 提取基础天气信息
            city = weather_data['data']['city']
            current_weather = weather_data['data']['current']

            temp = current_weather["temp"]
            humidity = current_weather["humidity"]
            weather = current_weather["weather"]
            visibility = current_weather["visibility"]

            return city, temp, humidity, weather, visibility

        except json.JSONDecodeError as e:
            print(f"JSON解析错误: {e}")
            return "ERROR"
        except KeyError as e:
            print(f"数据字段缺失: {e}")
            return "ERROR"


# noinspection PyMethodMayBeStatic
class Language:
    def LanguageList(self):
        try:
            with open(language_path, "rb") as f:
                language_list = tomllib.load(f)
                return True, language_list
        except FileNotFoundError:
            return False, traceback.format_exc()
        except Exception:
            return False, traceback.format_exc()

    def UpdateLanguageList(self):
        pass
        # TODO: 更新语言文件


# noinspection PyMethodMayBeStatic
class Vote:
    def new_item(self, cv, item_id, position):
        exec(f'item_name{item_id} = maliang.InputBox(cv, position, placeholder=f"项{item_id}", size=(300, 50), fontsize=26)')


class CloudControl:
    def GetCloudControl(self):
        pass


if __name__ == "__main__":
    a = Weather()
    print(a.get_weather("柳州市"))

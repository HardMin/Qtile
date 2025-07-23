import os
from random import randrange


class ScreenWallpaper:
    def __init__(self):
        self.__wallpapers_path = os.path.expanduser("~/.config/qtile/wallpaper")
        self.__wallpapers = os.listdir(f"{self.__wallpapers_path}")

    def __get_wallpaper(self, file):
        return f"{self.__wallpapers_path}/{file}"

    def _find_wallpaper_random(self):
        number_random = randrange(1, len(self.__wallpapers))
        if number_random > 0 and number_random < 10:
            number_random = f"0{number_random}"

        try:
            wallpaper = [
                wallpaper
                for wallpaper in self.__wallpapers
                if wallpaper.startswith(f"{number_random}")
            ][0]
        except IndexError:
            print(f"Wallpaper not found")
            return

        return self.__get_wallpaper(wallpaper)

    def _find_wallpaper(self, number):
        if number > 0 and number < 10:
            number = f"0{number}"

        try:
            wallpaper = [
                wallpaper
                for wallpaper in self.__wallpapers
                if wallpaper.startswith(f"{number}")
            ][0]
        except IndexError:
            print(f"Wallpaper {number} not found")
            return

        return self.__get_wallpaper(wallpaper)

    def aplicar_wallpaper(self, number=0):
        if number == 0:
            wallpaper = self._find_wallpaper_random()
        else:
            wallpaper = self._find_wallpaper(number)

        # test_notify(f'Wallpaper: {wallpaper}')
        os.system(f"feh --bg-fill {wallpaper}")

    def wallpaper(self):
        os.system("feh --bg-fill ~/Image/Wallpapers/6.jpg")


if __name__ == "__main__":
    wallpaper = ScreenWallpaper()
    wallpaper.aplicar_wallpaper()

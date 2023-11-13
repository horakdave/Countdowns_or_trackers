import datetime
import os
import time


target_date = datetime.date(2024, 4, 12)
days_until_target = (target_date - datetime.date.today()).days

wallpaper_path = os.path.join(os.path.expanduser('~'), 'Pictures', 'Wallpapers')
wallpaper_filename = 'countdown.jpg'
wallpaper_filepath = os.path.join(wallpaper_path, f'{days_until_target}_{wallpaper_filename}')

os.system(f'gsettings set org.gnome.desktop.background picture-uri "file://{wallpaper_filepath}"')

while True:
    days_until_target = (target_date - datetime.date.today()).days

    wallpaper_filepath = os.path.join(wallpaper_path, f'{days_until_target}_{wallpaper_filename}')

    os.system(f'gsettings set org.gnome.desktop.background picture-uri "file://{wallpaper_filepath}"')

    time.sleep(24 * 60 * 60)
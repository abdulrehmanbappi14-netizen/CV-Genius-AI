[app]

title = CV Genius AI
package.name = cvgeniusai
package.domain = org.cvgenius

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json

version = 0.1.0

requirements = python3,kivy==2.3.1,kivymd==1.2.0

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/assets/icons/icon.png
presplash.filename = %(source.dir)s/assets/images/presplash.png

[buildozer]

log_level = 2
warn_on_root = 1

[app:android]

android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 34
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a

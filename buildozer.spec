[app]

title = Batman Bakchodi
package.name = batmanbakchodi
package.domain = org.batman
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3
version = 1.0.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Internet permission is needed for future advertising integration.
android.permissions = android.permission.INTERNET

# Google Play new-app requirement from 31 Aug 2026: Android 16 / API 36.
android.api = 36
android.minapi = 23

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Google Play upload format.
android.release_artifact = aab
android.debug_artifact = apk

# Add an icon later when one is available.
# icon.filename = %(source.dir)s/icon.png

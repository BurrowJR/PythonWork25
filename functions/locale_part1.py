def extract_language(locale):
    parts = locale.split('_')
    language_code = parts[0]
    return language_code

print(extract_language('en_US.UTF-8'))
print(extract_language('en_GB.UTF-8'))
print(extract_language('ko_KR.UTF-16'))
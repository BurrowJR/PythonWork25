def extract_region(locale):
    parts = locale.split('_')    # 'en', 'US.UTF-8' 
    language_region = parts[1].split('.')[0]
    return language_region

print(extract_region('en_US.UTF-8'))
print(extract_region('en_GB.UTF-8'))
print(extract_region('ko_KR.UTF-16'))
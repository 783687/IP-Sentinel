import random
import os

# ==========================================================
# IP-Sentinel 超大型高保真指纹工厂 (V4.1.0 - 2025 年换代版)
# 核心功能: 升级指纹生命周期至 2025 年骨干型号，确保探测指纹真实度
# ==========================================================

def generate_chrome_version():
    # 模拟 2025 年主流 Chrome 内核号 (133 - 136)
    major = random.randint(133, 136)
    build = random.randint(6900, 7200)
    patch = random.randint(10, 150)
    return f"{major}.0.{build}.{patch}"

def generate_windows_ua(count=1000):
    uas = set()
    while len(uas) < count:
        uas.add(f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{generate_chrome_version()} Safari/537.36")
    return list(uas)

def generate_macos_ua(count=1000):
    uas = set()
    while len(uas) < count:
        mac_os_minor = random.randint(15, 16)
        mac_os_patch = random.randint(0, 4)
        if random.choice([True, False]):
            # Chrome on Mac
            uas.add(f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{mac_os_minor}_{mac_os_patch}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{generate_chrome_version()} Safari/537.36")
        else:
            # Safari on Mac (2025 年对应 Safari 18 系列)
            safari_build = f"618.1.{random.randint(10, 15)}"
            safari_version = f"18.{random.randint(1, 4)}"
            uas.add(f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{mac_os_minor}_{mac_os_patch}) AppleWebKit/{safari_build} (KHTML, like Gecko) Version/{safari_version} Safari/{safari_build}")
    return list(uas)

def generate_ios_ua(count=1000):
    uas = set()
    devices = ["iPhone", "iPad"]
    while len(uas) < count:
        device = random.choice(devices)
        ios_major = random.randint(18, 19)
        ios_minor = random.randint(1, 4)
        ios_patch = random.randint(0, 2)
        safari_build = f"618.1.{random.randint(10, 15)}"
        safari_version = f"{ios_major}.{random.choice(['0', '1', '2', '3'])}"
        
        uas.add(f"Mozilla/5.0 ({device}; CPU {'iPhone ' if device=='iPhone' else ''}OS {ios_major}_{ios_minor}_{ios_patch} like Mac OS X) AppleWebKit/{safari_build} (KHTML, like Gecko) Version/{safari_version} Mobile/15E148 Safari/604.1")
    return list(uas)

def generate_android_ua(count=1000):
    uas = set()
    # 2025 年迭代更新的主流智能移动端型号库 (如 Pixel 9系列, S25系列)
    models = [
        "Pixel 9 Pro", "Pixel 9", "Pixel 8a", "Pixel 9 Pro XL", 
        "SM-S938B", "SM-S938U", "SM-S931B", "SM-A566B", "SM-A366B", 
        "25011RKC6C", "24129PCD8G", "CPH2637", "V2427A", "PGT-AN20", "NX769J"
    ]
    while len(uas) < count:
        android_ver = random.randint(14, 15)
        model = random.choice(models)
        uas.add(f"Mozilla/5.0 (Linux; Android {android_ver}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{generate_chrome_version()} Mobile Safari/537.36")
    return list(uas)

if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)
    
    pool = []
    pool.extend(generate_windows_ua(1000))  
    pool.extend(generate_macos_ua(1000))    
    pool.extend(generate_ios_ua(1000))      
    pool.extend(generate_android_ua(1000))  
    
    with open('data/user_agents.txt', 'w') as f:
        for ua in pool:
            f.write(ua + '\n')
            
    print(f"✅ 成功生成 4000 条 2025 年高保真换代坐标指纹库！")
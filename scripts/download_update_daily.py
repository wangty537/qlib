""" 
每日增量更新：下载最新的 Qlib 数据但不删除旧数据
参考 download_init.py 的正确实现方式
"""
import os
import subprocess

# ===== 配置参数 =====
REGION     = "cn"                                   # "us" 或 "cn"
DATA_DIR   = os.path.abspath("./qlib_data/cn_data") # 保存目录
# ===================

os.makedirs(DATA_DIR, exist_ok=True)

cmd = [
    "python", "scripts/get_data.py",       # 使用 scripts 目录下的 get_data.py
    "qlib_data",
    "--target_dir", DATA_DIR,
    "--region", REGION,
    "--interval", "1d",
    "--delete_old", "False",               # 增量更新不删除旧数据
    "--exists_skip", "True"                # 如果数据已存在则跳过下载
]

print(">>> 开始增量更新...")
subprocess.run(cmd, check=True)
print(">>> 更新完成！")
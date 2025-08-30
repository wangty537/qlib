"""
首次运行：全量下载 Yahoo 股票日频数据并转成 Qlib 格式
无需关心源码，直接调用官方 CLI
"""
import os
import subprocess
from datetime import datetime

# ===== 用户只需改这 3 个变量 =====
REGION     = "cn"                                   # "us" 或 "cn"
DATA_DIR   = os.path.abspath("./qlib_data/cn_data") # 保存目录
START_DATE = "2000-01-01"
END_DATE   = datetime.today().strftime("%Y-%m-%d")
# ===============================

os.makedirs(DATA_DIR, exist_ok=True)

cmd = [
    "python", "scripts/get_data.py",       # 使用 scripts 目录下的 get_data.py
    "qlib_data",
    "--target_dir", DATA_DIR,
    "--region", REGION,
    "--interval", "1d",
    "--delete_old", "True"
]

print(">>> 开始全量下载...")
subprocess.run(cmd, check=True)
print(">>> 下载完成！")
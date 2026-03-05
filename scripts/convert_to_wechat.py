#!/usr/bin/env python3
"""
将 tech-daily 报告转换为微信公众号友好的格式。
- 去掉表格（公众号表格渲染差）
- 精简为 3-5 个重点
- 加上引导关注的结尾
- 输出为独立的 markdown 文件

用法: python3 convert_to_wechat.py reports/2026-03-05.md
"""

import sys
import os
import re
from datetime import datetime

def convert(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取日期
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', os.path.basename(input_path))
    date_str = date_match.group(1) if date_match else datetime.now().strftime('%Y-%m-%d')
    
    # 公众号版本模板
    wechat_article = f"""# 🔥 今日技术速报 | {date_str}

> 每天 3 分钟，掌握技术圈最新动态。

---

{content}

---

## 📬 关于本栏目

**每日技术速报** 由 AI 辅助生成，人工审核把关。

覆盖 AI / 后端 / 前端 / 安全 / 开源 等 14 大领域。

**觉得有用？点个「在看」，让更多人看到 👇**
"""
    
    # 输出路径
    output_dir = os.path.join(os.path.dirname(input_path), '..', 'wechat')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, os.path.basename(input_path))
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(wechat_article)
    
    print(f"✅ 公众号版本已生成: {output_path}")
    return output_path

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python3 convert_to_wechat.py <report_path>")
        sys.exit(1)
    convert(sys.argv[1])


数据来源自 English Review Book 文件

---
### 操作步骤
#### 1. 确保安装了 Python（3.6 以上）
在终端输入 `python --version` 或 `python3 --version` 检查。

#### 2. 创建 Python 脚本文件

新建一个文本文件，命名为 `convert.py`，复制以下全部代码：
```python
import re
import json
import sys
from datetime import datetime

def extract_expression(title_line):
    clean = title_line.lstrip('#').lstrip()
    clean = clean.strip('*').strip('=').strip()
    clean = clean.replace('*', '').replace('=', '').strip()
    return clean

def split_into_word_blocks(content):
    lines = content.split('\n')
    blocks = []
    current = []
    in_block = False
    for line in lines:
        if line.strip() == '#word':
            if in_block and current:
                blocks.append(current)
            current = []
            in_block = True
        if in_block:
            current.append(line)
    if in_block and current:
        blocks.append(current)
    return blocks

def parse_block(block_lines):
    body = block_lines[1:] if len(block_lines) > 1 else []
    if not body:
        return None

    title_line = ""
    content_start = 0
    for i, line in enumerate(body):
        if line.strip():
            title_line = line.strip()
            content_start = i + 1
            break
    if not title_line:
        return None

    expression = extract_expression(title_line)
    block_text = '\n'.join(body[content_start:])

    meaning = ""
    q_match = re.search(r'\?\s*\n\s*(.*)', block_text)
    if q_match:
        meaning = q_match.group(1).strip().split('\n')[0].strip()

    notes = []
    notes_match = re.search(r'\*\*Notes\*\*:\s*\n(.*?)(?=\n\*\*Sentences\*\*|\n<!--SR:|\Z)', block_text, re.DOTALL)
    if notes_match:
        for line in notes_match.group(1).strip().split('\n'):
            line = line.strip()
            if line and not line.startswith('<!--SR:'):
                line = re.sub(r'^[-*]\s+', '', line).strip()
                if line:
                    notes.append(line)

    sentences = []
    sent_match = re.search(r'\*\*Sentences\*\*:\s*\n(.*?)(?=\n<!--SR:|\Z)', block_text, re.DOTALL)
    if sent_match:
        pairs = re.findall(r'\*(.+?)\*\s*\n(.+?)(?=\n\*|<!--SR:|\Z)', sent_match.group(1), re.DOTALL)
        for eng, chn in pairs:
            sentences.append((eng.strip(), chn.strip()))

    return {
        "expression": expression,
        "meaning": meaning,
        "notes": notes,
        "sentences": sentences
    }

def create_import_json(md_path, output_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('\r\n', '\n')

    blocks = split_into_word_blocks(content)
    words = []
    all_sentences = []
    word_id = 1
    sent_id = 1
    now_ts = int(datetime.now().timestamp())

    for block in blocks:
        parsed = parse_block(block)
        if not parsed:
            continue

        sent_ids = []
        for eng, chn in parsed['sentences']:
            all_sentences.append({
                "text": eng,
                "trans": chn,
                "origin": "",
                "id": sent_id
            })
            sent_ids.append(sent_id)
            sent_id += 1

        words.append({
            "expression": parsed['expression'],
            "meaning": parsed['meaning'],
            "status": 1,
            "t": "WORD",
            "notes": parsed['notes'],
            "sentences": sent_ids,
            "tags": [],
            "connections": [],
            "date": now_ts,
            "id": word_id,
            "$types": {
                "sentences": "set",
                "tags": "set",
                "connections": "map"
            }
        })
        word_id += 1

    import_data = {
        "formatName": "dexie",
        "formatVersion": 1,
        "data": {
            "databaseName": "WordDB",
            "databaseVersion": 1,
            "tables": [
                {"name": "expressions", "schema": "++id,&expression,status,t,date,*tags", "rowCount": len(words)},
                {"name": "sentences", "schema": "++id,&text", "rowCount": len(all_sentences)}
            ],
            "data": [
                {"tableName": "expressions", "inbound": True, "rows": words},
                {"tableName": "sentences", "inbound": True, "rows": all_sentences}
            ]
        }
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(import_data, f, ensure_ascii=False, indent=2)

    print(f"转换完成！共导出 {len(words)} 个单词/短语，{len(all_sentences)} 个句子。")
    print(f"已保存至: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python convert.py 你的markdown文件.md")
    else:
        md_input = sys.argv[1]
        create_import_json(md_input, "import.json")
```

~~~python

import re
import json
import sys
from datetime import datetime

def extract_expression(title_line):
    clean = title_line.lstrip('#').lstrip()
    clean = clean.strip('*').strip('=').strip()
    clean = clean.replace('*', '').replace('=', '').strip()
    return clean

def split_into_word_blocks(content):
    lines = content.split('\n')
    blocks = []
    current = []
    in_block = False
    for line in lines:
        if line.strip() == '#word':
            if in_block and current:
                blocks.append(current)
            current = []
            in_block = True
        if in_block:
            current.append(line)
    if in_block and current:
        blocks.append(current)
    return blocks

def parse_block(block_lines):
    body = block_lines[1:] if len(block_lines) > 1 else []
    if not body:
        return None

    title_line = ""
    content_start = 0
    for i, line in enumerate(body):
        if line.strip():
            title_line = line.strip()
            content_start = i + 1
            break
    if not title_line:
        return None

    expression = extract_expression(title_line)
    block_text = '\n'.join(body[content_start:])

    meaning = ""
    q_match = re.search(r'\?\s*\n\s*(.*)', block_text)
    if q_match:
        meaning = q_match.group(1).strip().split('\n')[0].strip()

    notes = []
    notes_match = re.search(r'\*\*Notes\*\*:\s*\n(.*?)(?=\n\*\*Sentences\*\*|\n<!--SR:|\Z)', block_text, re.DOTALL)
    if notes_match:
        for line in notes_match.group(1).strip().split('\n'):
            line = line.strip()
            if line and not line.startswith('<!--SR:'):
                line = re.sub(r'^[-*]\s+', '', line).strip()
                if line:
                    notes.append(line)

    sentences = []
    sent_match = re.search(r'\*\*Sentences\*\*:\s*\n(.*?)(?=\n<!--SR:|\Z)', block_text, re.DOTALL)
    if sent_match:
        pairs = re.findall(r'\*(.+?)\*\s*\n(.+?)(?=\n\*|<!--SR:|\Z)', sent_match.group(1), re.DOTALL)
        for eng, chn in pairs:
            sentences.append((eng.strip(), chn.strip()))

    return {
        "expression": expression,
        "meaning": meaning,
        "notes": notes,
        "sentences": sentences
    }

def create_import_json(md_path, output_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('\r\n', '\n')

    blocks = split_into_word_blocks(content)
    words = []
    all_sentences = []
    word_id = 1
    sent_id = 1
    now_ts = int(datetime.now().timestamp())

    for block in blocks:
        parsed = parse_block(block)
        if not parsed:
            continue

        sent_ids = []
        for eng, chn in parsed['sentences']:
            all_sentences.append({
                "text": eng,
                "trans": chn,
                "origin": "",
                "id": sent_id
            })
            sent_ids.append(sent_id)
            sent_id += 1

        words.append({
            "expression": parsed['expression'],
            "meaning": parsed['meaning'],
            "status": 1,
            "t": "WORD",
            "notes": parsed['notes'],
            "sentences": sent_ids,
            "tags": [],
            "connections": [],
            "date": now_ts,
            "id": word_id,
            "$types": {
                "sentences": "set",
                "tags": "set",
                "connections": "map"
            }
        })
        word_id += 1

    import_data = {
        "formatName": "dexie",
        "formatVersion": 1,
        "data": {
            "databaseName": "WordDB",
            "databaseVersion": 1,
            "tables": [
                {"name": "expressions", "schema": "++id,&expression,status,t,date,*tags", "rowCount": len(words)},
                {"name": "sentences", "schema": "++id,&text", "rowCount": len(all_sentences)}
            ],
            "data": [
                {"tableName": "expressions", "inbound": True, "rows": words},
                {"tableName": "sentences", "inbound": True, "rows": all_sentences}
            ]
        }
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(import_data, f, ensure_ascii=False, indent=2)

    print(f"转换完成！共导出 {len(words)} 个单词/短语，{len(all_sentences)} 个句子。")
    print(f"已保存至: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python convert.py 你的markdown文件.md")
    else:
        md_input = sys.argv[1]
        create_import_json(md_input, "import.json")
~~~
#### 3. 运行脚本

把 `convert.py` 和你之前提供的 `生词复习（space-repetation）.md` 放在同一目录下，打开终端执行：

~~~bash

python convert.py "生词复习（space-repetation）.md"
~~~
如果名字不同，替换成你实际的 md 文件名。

#### 4. 导入到 Obsidian
脚本运行后会在当前目录生成 `import.json`。  
在 Language Learner 面板点击 **“导入”**，选择该文件，即可覆盖当前空数据库，把所有单词导入。
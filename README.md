# 今天boris叫我来巡山。。。
### 哦，不。。搞一下申请软著的代码，120页代码一页一页复制手都断了，于是就有了这个东西。。
### 软著 简称ruan zhu(rz)，
> 故使用方法：
* python rz.py
> 配置文件 config.json：
```
{
  # 你想要游走的项目路径。
  "walk_dir": "/your-project-dir",

  # 在每一个文件初始时需要带一个 完整路径/仅文件名 的头吗？
  "with_filepath?": false,
  "with_filename?": true,
  
  # 行首发现以下字符跳过（用于跳过注释）
  "skip_when_character": [
    "#",
    "!",
    "\n",
    "\r",
    "/",
    " /",
    " *"
  ],
  # 你需要扒那些文件？
  "allow_files_suffix": [
    ".js",
    ".jsx",
    ".rb",
    ".ts",
    ".tsx"
  ],
  # 输出在哪里？
  "output_filename": "out1.txt"
}
```
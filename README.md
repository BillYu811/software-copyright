# software-copyright
#今天boris叫我来巡山。。。
###哦，不。。搞一下申请软著的代码，120页代码一页一页复制手都断了，于是就有了这个东西。。

###软著 简称ruan zhu(rz)，
> 故使用方法：
* python rz.py
> 配置：
```
{
  "walk_dir": "/your-project-dir",
  "with_filepath?": false,
  "with_filename?": true,
  "skip_when_character": [
    "#",
    "!",
    "\n",
    "\r",
    "/",
    " /",
    " *"
  ],
  "allow_files_suffix": [
    ".js",
    ".jsx",
    ".rb",
    ".ts",
    ".tsx"
  ],
  "output_filename": "out1.txt"
}
```
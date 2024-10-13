import os

def create_index_html(root_dir='.'):  
    # 准备HTML模板  
    html_content = ""

    # 遍历目录树  
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames.sort()
        # 遍历当前目录下的文件  
        for filename in sorted(filenames):
            if '.pdf' in filename:  
                # 生成HTML超链接，注意处理路径中的特殊字符  
                relative_path = os.path.relpath(os.path.join(root_dir, dirpath, filename), root_dir)
                html_content += f"<li><a href=\"js/pdf/web/viewer.html?file=/src/subjects/{relative_path}\">{filename}</a></li>\n"
            elif '.py' not in filename:
                relative_path = os.path.relpath(os.path.join(root_dir, dirpath, filename), root_dir)
                html_content += f"<li><a href=\"./src/subjects/{relative_path}\">{filename}</a></li>\n"
    
    #print(html_content)
    return html_content

if __name__ == "__main__":  
    # 准备HTML模板                              
    html_content = """
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>学习资料</title>
        </head>
    <body>"""

    directory_path = os.getcwd()
    dirnames=[]

    # 列出目录下的所有文件和文件夹  
    for item in os.listdir(directory_path):  
        # 拼接完整路径  
        full_path = os.path.join(directory_path, item)  
        # 判断是否为目录  
        if os.path.isdir(full_path):  
            dirnames.append(item)

    for dirname in dirnames:
        print(dirname)
        html_content+=f"<p>{dirname}</p>\n"
        html_content+=create_index_html(dirname)

    # 结束HTML模板                          
    html_content+= """
        </ul>
    </body>
    </html>"""

    with open("resources.html","w",encoding='utf-8') as f:
        f.write(html_content)
        f.close()

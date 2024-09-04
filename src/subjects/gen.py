import os

def create_index_html(root_dir='.'):  
    # 准备HTML模板  
    html_content = """  
    <!DOCTYPE html>  
    <html>  
    <head>  
        <title>Index of {}</title>  
    </head>  
    <body>  
        <h1>Index of {}</h1>  
        <ul>  
    """.format(root_dir, root_dir) 

    # 遍历目录树  
    for dirpath, dirnames, filenames in os.walk(root_dir):  
        # 遍历当前目录下的文件  
        for filename in filenames:  
            # 排除隐藏文件（以'.'开头的文件）  
            if not filename.startswith('.'):  
                # 生成HTML超链接，注意处理路径中的特殊字符  
                relative_path = os.path.relpath(os.path.join(dirpath, filename), root_dir)  
                # 使用urllib.parse.quote对路径进行编码，以避免特殊字符问题（可选）  
                # 但在这里为了简单起见，我们假设路径不包含需要编码的字符                        
                html_content += f"<li><a href=\"js/pdf/web/viewer.html?file=/src/subjects/{relative_path}\">{filename}</a></li>\n"  
                                                    # 结束HTML模板  
    html_content+= """
        </ul>
    </body>  
    </html>                                         """
                                                    # 写入index.html文件
    with open('resources.html', 'w') as f:
        f.write(html_content)

    print("resources.html has been created successfully.")

if __name__ == "__main__":  
    create_index_html()

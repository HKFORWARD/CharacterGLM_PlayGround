# import time
# from dotenv import load_dotenv
# load_dotenv()

# from api import get_characterglm_response

# def auto_dialogue():
#     # 角色的详细信息和元数据
#     characters = {
#         "小白": {
#             "info": "小白，性别女，17岁，平溪孤儿院的孩子。小白患有先天的白血病，头发为银白色。",
#             "role": "assistant",
#             "name": "小白"
#         },
#         "阿南": {
#             "info": "阿南，性别男，22岁，也是平溪孤儿院的孩子。阿南非常关心小白。",
#             "role": "user",
#             "name": "阿南"
#         }
#     }

#     # 初始化对话历史
#     history = [
#         {"role": "assistant", "content": "阿南哥哥，我会死吗？", "name": "小白"},
#         {"role": "user", "content": "怎么会呢？医生说你的病情已经好转了", "name": "阿南"}
#     ]

#     for _ in range(6):  # 设置对话轮数
#         last_message = history[-1]
#         # 根据当前角色切换到另一个角色
#         new_role = "assistant" if last_message['role'] == "user" else "user"
#         new_name = "小白" if last_message['name'] == "阿南" else "阿南"

#         response_generator = get_characterglm_response([last_message], meta=characters[new_name])
#         # response_content = "".join(response_generator)  # 连接生成器的所有输出成一个字符串
#         # response_content = " ".join(chunk for chunk in response_generator)  # 迭代生成器收集回答

#         # 检查生成器内容
#         if response_generator:
#             response_content = " ".join(chunk for chunk in response_generator if isinstance(chunk, str))
#             if response_content == "":
#                 print("警告：生成的回应为空")
#         else:
#             print("错误：未从API获取到任何响应")
#             response_content = "没有回应"
            
#         history.append({"role": new_role, "content": response_content, "name": new_name})
#         print(f"{new_name} says: {response_content}")
#         time.sleep(0.25)

# if __name__ == "__main__":
#     auto_dialogue()


import time
from dotenv import load_dotenv
load_dotenv()

from api import get_characterglm_response

def auto_dialogue():
    # 定义两个角色的人设
    character_meta = {
        "周迎雪": {
            "info": "周迎雪，性别女，25岁，超凡者，能力是植物。气质美女，杨氏间谍。",  # 示例描述
            "name": "周迎雪"
        },
        "任小粟": {
            "info": "任小粟，性别男，18岁，超凡者，能力多样，最重要的是复刻他人的能力。",
            "name": "任小粟"
        }
    }
    
    # 初始化对话历史
    history = [
        {"role": "assistant", "content": "你好啊。", "name": "周迎雪"},
        {"role": "user", "content": "阿姨好。", "name": "任小粟"}
    ]

    # 自动对话生成
    for _ in range(20):
        last_message = history[-1]
        new_role = "assistant" if last_message['role'] == "user" else "user"
        new_name = "周迎雪" if last_message['name'] == "任小粟" else "任小粟"

        response_generator = get_characterglm_response([last_message], meta=character_meta[new_name])
        
        # 迭代生成器以获取完整的响应
        response_content = "".join(response_generator)  # 将生成的所有片段连接成一个字符串
        
        history.append({"role": new_role, "content": response_content, "name": new_name})
        print(f"{new_name} says: {response_content}")
        time.sleep(0.25)
        
if __name__ == "__main__":
    auto_dialogue()

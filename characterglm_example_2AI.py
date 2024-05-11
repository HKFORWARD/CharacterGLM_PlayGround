import time
from dotenv import load_dotenv
load_dotenv()

from api import get_characterglm_response

def auto_dialogue(num_turns=20):
    # 定义两个角色的人设
    character_meta = {
        "bot_info": "周迎雪，性别女，25岁，超凡者，一开始是壁垒人，能力是植物。气质美女，杨氏间谍。杨氏覆灭前曾监视任小粟。这段对话的主题是周迎雪在图书馆想找任小粟聊天套有用情报。因为杨氏不相信任小粟只是简单的流民。",
        "bot_name": "周迎雪",
        "user_info": "任小粟，性别男，18岁，超凡者，一开始是流民。超凡能力多样，最重要的是复刻他人的能力。一开始就认出了周迎雪是间谍来监视他，并不想暴露自己是顶级超凡者的身份。他对周迎雪十分冷淡，而且经常戏耍她。",
        "user_name": "任小粟"
    }
        
    # 初始化对话历史
    history = [
        {"role": "assistant", "content": "（慢慢的走到对面坐下，笑道）你好啊。"},
        {"role": "user", "content": "（抬头道）阿姨好。"},
        # {"role": "assistant", "content": "（周迎雪听到被叫阿姨，很不开心，毕竟自己才25岁，而且算是来色诱。她收拾了下心情）我年纪做你姐姐还差不多，你对这图书馆熟吗？"},
        # {"role": "user", "content": "（当然任小粟也不是真觉得对方年纪大,纯粹是懒得搭理她，只想好好养伤）不熟"},
        # {"role": "assistant", "content": "（周迎雪顿了一下，你天天来这图书馆，这都快半个月了，还说自己不熟？她继续笑着说道）我想找一本叫做时间概论的书，你知道在哪放着吗？"},
        # {"role": "user", "content": "（任小粟没料到对方要硬聊，本不想理会。然后这时接到了任务要求他为求知者找到书籍的正确位置。任务必须做，他看了周迎雪一眼试探道）时间概论肯定就在这个图书馆里，要不你自己找找？"},
        # {"role": "assistant", "content": "（周迎雪愣了一下，你怎么不说书在88壁垒里呢？我当然知道书就在这图书馆里！周迎雪在图书馆工作人员的帮助下找到了书开始看，周迎雪是一肚子的火想发却发不出来。）那，还是谢谢，我问问图书馆里员吧。"},
        # {"role": "user", "content": "（不过任小粟不管那么多，反正任务要求的是正确位置，他说书就在这图书馆里也不能算错啊，是不是？）好"},
        # {"role": "assistant", "content": "（周迎雪进图书馆之后，竟然脱掉了大衣，显露出里面修身的旗袍来。）好热啊。"},
        # {"role": "user", "content": "（任小粟拿了一本《大王饶命》到对方面前）你好。"},
        # {"role": "assistant", "content": "（周迎雪等到对方靠近才抬起头来）你好，有事吗？"},
        # {"role": "user", "content": "（任小粟把手里的《大王饶命》放在面前）我觉得这套书挺有意思，你看看。"},
        # {"role": "assistant", "content": "（周迎雪则翻开面前的书本，看了一会儿，周迎雪觉得很好笑。一下午啥也没干，光在哪里傻乐呵，笑得像神经病一样）哈哈哈哈，这本书太搞笑了，哈哈哈。"},
        # {"role": "user", "content": "（任小粟鄙夷的说）现在没有气质没有吸引力了吧，还想色诱我呢？"},
        # {"role": "assistant", "content": "（下午走的时候，周迎雪走到对方面前）你的书太有趣了，我肚子都要笑破了。特别是那句：‘“班长别伤心，虽然你的个子不高，但你…发际线高啊！’"},
        # {"role": "user", "content": "（任小粟心说这果然是专门套近乎的人啊，给根杆子就能往上爬的选手。于是冷冷的说）这本书以主角的视角看很爽，但你一旦站在第三人的角度去看主角与旁人的互动，就会觉得――为何会有这么讨厌的人。"},
        # {"role": "assistant", "content": "（周迎雪明显感觉到对方的冷漠，但是还是热情的问道）还有没有这么好看的书啊？我过几天看完了该看啥呢？"},
        # {"role": "user", "content": "（任小粟心说得给她写难懂的书，这样慢慢的就不找我了。）这本《史记》不错，还有《物理学原理》和《The Principles of Mathematics》也很好看。"},
        # {"role": "assistant", "content": "（任小粟出图书馆的时候看到周迎雪站在门口，任小粟假装没看到她要出去，周迎雪喊住他）你有空吗？有件事情不知道能不能说？"},
        # {"role": "user", "content": "没空"},
        # {"role": "assistant", "content": "（周迎雪略显尴尬，正准备怎么回复）"},
        # {"role": "user", "content": "（任小粟得到宫殿的任务去帮助求助的女人，马上变脸回复）现在又有空了，你说怎么帮你吧"},
        # {"role": "assistant", "content": "（周迎雪愣了两秒，但她很快便调整情绪笑道）今天是我生日，但是我在壁垒里已经没有亲人了，今晚你能陪陪我吗？"},
        # {"role": "user", "content": "（任小粟有点牙疼了）怎么陪？"},
        # {"role": "assistant", "content": "（周迎雪轻笑着说道）去我家吧，咱们玩点游戏"},
        # {"role": "user", "content": "（任小粟已经有点想放弃这任务了）玩什么游戏？"},

        # {"role": "assistant", "content": "（周迎雪眨巴着眼睛看向任小粟）一个人玩不了的游戏"},
        # {"role": "user", "content": "（一个人玩不了的游戏嘛，任小粟略加思考问道）跳皮筋吗？我跳皮筋贼厉害！"},
        # {"role": "assistant", "content": "（周迎雪很无语，回答道）两个人也玩不了跳皮筋啊……"},
        # {"role": "user", "content": "（这时图书馆管理员从图书馆里走了出来，眼看着要锁门了，任小粟说道）你看，人凑齐了！"},
        # {"role": "assistant", "content": "（周迎雪尴尬笑道）算了，不玩了。"},
        # {"role": "user", "content": "（任小粟看了一眼宫殿里的任务）不行，必须玩！"},

        # {"role": "assistant", "content": "（周迎雪真是情绪管理的高手）那好，我们三个一起玩，到我家去吧"},
        # {"role": "user", "content": "（拿出皮筋并说道）就这里吧"},
        # {"role": "assistant", "content": "（周迎雪有点惊讶）好吧，那我们就在这里玩"},
        # {"role": "user", "content": "（半小时后任小粟得到了任务完成的提示，于是马上往家里跑，什么也没说）"},
        # {"role": "assistant", "content": "（周迎雪有点手足无措）哎，你就这么走了？"},
        # {"role": "user", "content": "（懒得多数，边跑边喊）突然想起来家里有点事。明天见。你也回家吧，时间也不早了。"},
    ]
    
    # # 对话轮次
    # num_turns = 20  # 设定一个对话的轮次，这里我们做6轮对话
    
    # # 自动对话生成
    for _ in range(num_turns):
        last_message = history[-1]
        new_role = "assistant" if last_message['role'] == "user" else "user"
        new_name = "周迎雪" if last_message['role'] == "user" else "任小粟"
        
        response_generator = get_characterglm_response([last_message], meta=character_meta)
        
        # 迭代生成器以获取完整的响应
        response_content = "".join(response_generator)  # 将生成的所有片段连接成一个字符串
        
        history.append({"role": new_role, "content": response_content})
        print(f"{new_name}: {response_content}")
        time.sleep(0.1)
        
if __name__ == "__main__":
    auto_dialogue()
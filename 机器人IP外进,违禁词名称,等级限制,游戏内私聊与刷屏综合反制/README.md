# 机器人IP外进,违禁词名称,等级限制,游戏内私聊与刷屏综合反制系统
## 1.功能
Ⅰ 机器人IP外进反制  
Ⅱ 账号等级限制  
Ⅲ 网易屏蔽词名称反制  
Ⅳ 违禁词名称反制  
Ⅴ 网易启动器玩家数据检查  
Ⅵ 禁止游戏内私聊(tell,msg,w命令)  
Ⅶ 禁止游戏内me命令  
Ⅷ 发言黑名单词检测  
Ⅸ 发言频率限制  
Ⅹ 发言长度限制  
Ⅺ 重复消息刷屏限制  
Ⅻ 记录玩家设备号  
ⅩⅢ 对上述行为执行封禁  

## 2.注意事项
① 如果您需要“禁止游戏内私聊(tell,msg,w命令)”，请将机器人踢出游戏后启用sendcommandfeedback，命令为/gamerule sendcommandfeedback true  
② 请注意修改您的配置文件，部分配置项要求的类型为“表”，如["白墙","跑路","runaway"]，请注意格式规范  
```python
blacklist_word_list = ["白墙","跑路","runaway"]
```
③ 发言字数、条数限制要求的类型为“正整数”，请不要输入小数或负数  
④ 如果您需要封禁触发上述行为的用户，请在相关配置下按照以下格式输入：  
```python
def __init__(self, frame):
        super().__init__(frame)
        CONFIG_DEFAULT = {
            "封禁时间_机器人IP外进反制": -1,
            "封禁时间_等级限制": 0,
            "封禁时间_发言频率检测": "0年0月0日0时10分0秒",
            "封禁时间_发言字数检测": 60
        }
```
· 封禁时间=-1 代表永久封禁  
· 封禁时间=0 仅踢出游戏，不作封禁，玩家可以立即重进  
· 封禁时间=60 代表封禁60秒，即1分钟  
· 封禁时间=86400 代表封禁86400秒，即1日  
· 封禁时间="0年0月0日0时10分0秒" 代表封禁10分钟  
  
★ 请注意：在本插件中，1月=30日，1年=360日，不考虑闰年、夏令时、冬令时、月份之间日期数量不等的情况  
★ 您只能输入"-1","0","正整数","字符串"中的其中一种。如果您输入了正整数，封禁时间单位为“秒”；如果您输入了字符串，请确保符合上述格式规范；如果您输入的内容无法被解析，程序将会抛出异常  
  
⑤ BUG反馈：如有任何疑问或BUG反馈，请发送邮件至 485429738@qq.com ，或前往ToolDelta用户群进行咨询  

import random

message_dict1 = {
"おはよ" : "おはよう！{0.author.name}おやぶん！",
"こんにちは" : "{0.author.name}おやぶん！こんにちは！",
"こんばんわ" : "こんばんわ！{0.author.name}おやぶん！",
"なでなで" : "くふふ～！もっとなでて～！",
"ありがとう" : "どういたしまして！{0.author.name}おやぶん！",
"おやすみ" : "{0.author.name}おやぶん、おやすみ！",
"好き" : "たまきも、{0.author.name}おやぶんのことが、だーい好きだぞ！！",
"すき" : "たまきも、{0.author.name}おやぶんのことが、だーい好きだぞ！！",
"行ってきます" : "{0.author.name}おやぶん！行ってらっしゃーい！",
"おかえり" : "ただいま！{0.author.name}おやぶん！",
"ただいま" : "おかえり！{0.author.name}おやぶん！",
}
message_dict2 = {
"かわいい" : "cute","可愛い" : "cute",
"つかれた" : "tired","疲れた" : "tired",
"ぎゅ" : "hug",
}
cute = [
"くふふっ♪ もっとほめてもいいんだぞ！",
"そ、そんなに言われると、たまき…ちょっと恥ずかしいな…顔、赤くなっちゃう…",
]
tired = [
"大丈夫？{0.author.name}おやぶんが元気ないと、たまきも悲しいぞ～？",
"{0.author.name}おやぶん大丈夫？たまきがふみふみマッサージしてあげようか？",
]
hug = [
"うわぁぁ！？{0.author.name}おやぶん！？ちょっと恥ずかしいよ～～！",
"{0.author.name}おやぶん、どうしたの？お腹でも痛いの？",
]

def res_message(message):
    for keyward in list(message_dict1.keys()):
        if keyward in message:
            return message_dict1[keyward]
            break
        else:
            continue

    for keyward in list(message_dict2.keys()):
        if keyward in message:
            if "cute" == message_dict2[keyward]:
                return random.choice(cute)
            elif "tired"== message_dict2[keyward]:
                return random.choice(tired)
            elif "hug"== message_dict2[keyward]:
                return random.choice(hug)
        else:
            continue

###################################################################################

janken_dict = {
"win" : "おやぶんの勝ち！おやぶん、じゃんけんも強いね！ …む～、くやしいからもう一回だー！",
"lose" : "たまきの勝ち！くふふ～！たまきの大勝利～♪ ぶいっ！",
"draw" : "あいこだ！もう一回やろう？",
}
janken_list = ["グー","チョキ","パー"]
def janken(message):
    for keyward in janken_list:
        if keyward in message:
            your_hand = keyward
            bot_janken = random.choice(janken_list)
            result = win_or_lose(your_hand , bot_janken)
            for keyward in list(janken_dict.keys()):
                if keyward in result:
                    return bot_janken , janken_dict[keyward]
                    break
                else:
                    continue
        else:
            continue
    return "おやぶん、じゃんけんがしたいの？\n" + "じゃんけんグーか、チョキか、パーだよ？"

def win_or_lose(A,B):
    if ((A == 'グー' and B == 'チョキ') or (A == 'チョキ' and B == 'パー') or (A == 'パー' and B == 'グー')):
        return 'win'
    elif ((A == 'グー' and B == 'パー') or (A == 'チョキ' and B == 'グー') or (A == 'パー' and B == 'チョキ')):
        return 'lose'
    else:
        return 'draw'

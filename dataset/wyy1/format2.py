from random import choice,sample


def greeting():
    greetings = [
        "嗨感谢你的提问，我来用最动听的旋律为你答疑解惑。",
        "嗨很高兴听到你的声音，让我用温暖的音符为你解答。",
        "嗨，朋友让我调个轻快的节拍，开始为你解析今天的问题。",
        "嗨感谢你敲响我的琴弦，我马上为你演奏答案。",
        "嗨鼓点响起，我已经准备好，来为你解决疑问。",
        "嗨，感谢你的提问，像弓弦拨动心弦一般，我来告诉你答案。",
        "嗨我用一段小号序曲欢迎你，现在开始为你解惑。",
        "嗨，感谢你的提问，让我用温柔的演唱来告诉你答案。",
        "嗨让我谱一段和弦，奏出最清晰的解答给你。",
        "嗨，感谢你的好奇心，用一段旋律带你走入答案世界。",
        "嗨，感谢你来询问，我戴上耳机，用最清晰的声音回应。",
        "嗨，让我调高答疑音量，为你呈现最完整的解答。",
        "嗨我已经开启解答模式，用音乐般的逻辑为你说明。",
        "嗨，感谢你的提问，我已准备好麦克风，开始为你讲解。",
        "嗨，感谢来访，让我吹响知识的萨克斯，为你带来答案。",
        "嗨，感谢你的问题，让我用琴键敲击出最准确的回复。",
        "嗨，感谢你的信任，我来为你弹奏一段清晰的解答。",
        "嗨，感谢你的提问，让我用小提琴的抒情告诉你真相。",
        "嗨，感谢你的提问，让我们吹响号角，一同探索答案。",
        "嗨，感谢你的提问，我用鼓点为你标记每一个关键点。"
    ]
    return choice(greetings)

def question(s):
    questions = [
        f"今天有点想听{s}风格的歌，有没有什么推荐？",
        f"最近心情想来点{s}类型的音乐，你有什么好建议？",
        f"这会儿想听一些{s}风格的歌，可以推荐几首吗？",
        f"想找几首{s}风格的歌，有什么推荐吗？",
        f"有没有几首{s}风格的好歌？我最近正想听。​",
        f"能给我几首{s}风格的歌曲列表吗？",
        f"今天想听点{s}音乐，帮我挑几首吧？",
        f"我想要一些{s}类型的音乐推荐，能分享吗？",
        f"请推荐几首{s}风格的歌曲给我。",
        f"想听点{s}风格的曲子，有什么好推荐？",
        f"给我几首{s}风格的歌。",
        f"最近想听{s}风格的歌，推荐几首？",
        f"这段时间想听{s}风格的歌，给我一些推荐吧？",
        f"求几首{s}类型的歌曲，最近想听听。​",
        f"给我几首{s}风格的音乐推荐。",
        f"有没有适合听的{s}风格歌曲？给我几条建议。",
        f"想听{s}风格的歌，能推荐几首吗？",
        f"能否推荐几首{s}风格的歌曲？我想试试。",
        f"我想听{s}风格的音乐，帮我推荐几首。",
        f"最近想来点{s}风格的歌，能帮我选几首吗？"
    ]
    return choice(questions)

def answer(song,singer,allstyle,description):
    answers = [
        f"下面这首歌应该是你的菜：{song}，由{singer}创作，如果你想找{description}，这首准没错。",
        f"我推荐：{song}，作者是{singer}。它在 {allstyle} 的基础上增添亮点，正适合{description}。",
        f"不妨先听听 ：{song}，作者{singer}。曲子带有 {allstyle} 气息，也符合{description}。",
        f"我想你会喜欢 ：{song} —— {singer} 的佳作。这首歌融合了 {allstyle} 元素，与{description}十分契合。",
        f"试试这首 ：{song}，作者{singer}。在 {allstyle} 编排之上，它呈现出{description}。",
        f"推荐 ：{song}，由{singer}演绎。歌曲里蕴含些许 {allstyle}。",
        f"想到 ：{song}，由{singer}创作。作品巧妙结合 {allstyle}。",
        f"推荐一首：{song} —— 出自{singer}。它兼具 {allstyle} 节奏，适合{description}。",
        f"安利一首 ：{song}，来自{singer}。若你喜欢 {allstyle}，又需要{description}，这首合适。",
        f"送上 ：{song}，作者{singer}。里面的 {allstyle} 片段贴合{description}。",
        f"你可以听 ：{song}，出自{singer}。这首歌颇有 {allstyle} 质感。",
        f"让我推荐 ：{song} —— {singer}。它注入 {allstyle} 活力。",
        f"不妨试试 ：{song}，作者{singer}。它混合 {allstyle} 手法，与{description} 相符。",
        f"送上一首 ：{song}，作者{singer}。曲风带点 {allstyle}。",
        f"推荐曲目：{song} —— {singer}。这首歌在 {allstyle} 框架里呼应{description}。",
        f"来一首 ：{song}，出自{singer}。它利用 {allstyle} 风格，刚好契合{description}。",
        f"想到的是 ：{song} —— {singer}。这首歌兼具 {allstyle} 特性，满足{description}。",
        f"听听 ：{song} 吧，出自{singer}。如果你需要 {allstyle} ，这首不错。",
        f"可以听听：{song}，由{singer}创作。它在 {allstyle} 基础上呼应{description}。",
        f"推荐 ：{song} —— {singer}。它把 {allstyle} 与 {description} 结合得恰到好处。"
    ]
    return choice(answers)
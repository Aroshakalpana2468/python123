from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from mongodb import all_users, all_groups, add_user, add_group


bot = Client(
    "my first project",
    api_id = 7622044,
    api_hash = "1fcd3dd600503aa1ebc5033b58016264",
    bot_token = "5148488712:AAHahhs2uKE2N7KmgnzfAWLJ2RiVXrsLE0s"
)

SUDO_ID = "1844047320"
SUDO = [int(x) for x in SUDO_ID.split()]
START_MESSAGE = "Heya, I am a simple test bot"
START_MESSAGE_BUTTONS = [
    [
        InlineKeyboardButton('CHANNEL', url= 'https://t.me/pc1games12'),
        InlineKeyboardButton('GROUP1', url= 'https://t.me/aastrem')
    ],
    [
        InlineKeyboardButton('GROUP2', url= 'https://t.me/slfreefire23'),
        InlineKeyboardButton('GROUP3', url= 'https://t.me/SL_FREE_FIRE')   
    ]

]


@bot.on_message(filters.command('start') & filters.private)
def start(bot, message):
   text = START_MESSAGE
   reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
   message.reply(
       text=text,
       reply_markup=reply_markup,
       disable_web_page_preview=True
   )
   if message.chat.type == "private" : add_user(message.from_user.id)
   if message.chat.type != "private" : add_group(message.chat.id)  
        
        
REPLY_MESSAGE = "choose a button below!"

REPLY_MESSAGE_BUTTONS = [
    [
      ("hi"),
      ("hello"),
    ],
    [
        ("my master"),
        ("thnx")
    ]
]

@bot.on_message(filters.command('greet'))
def greet(bot, message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )

@bot.on_message(filters.regex("hi"))
def reply_to_hi(bot, message):
    bot.send_message(message.chat.id, "Hello!")

@bot.on_message(filters.regex("hello"))
def reply_to_hello(bot, message):
    bot.send_message(message.chat.id, "Hi!")

@bot.on_message(filters.regex("my master"))
def reply_to_my_master(bot, message):
    bot.send_message(message.chat.id, "@BUDDY3_FF")

@bot.on_message(filters.regex("thnx"))
def reply_to_thnx(bot, message):
    bot.send_message(message.chat.id, "me mage python use karala hadapu palaweni bot????????. bot hodada nadda kiyala mata therenne naa..  bot start karata THNX????????????.. ehema mama giya BYE")

@bot.on_message(filters.command('help'))
def command1(bot, message):
    message.reply_text("This is test bot's help section.")

#welcomebot
GROUP = "ak_live_stream_2"
WELCOME_MESSAGE = "Hello, welcome to group chat!"

@bot.on_message(filters.chat(GROUP) & filters.new_chat_members)
def welcomebot(client, message):
    message.reply_text(WELCOME_MESSAGE)


#send_photo
@bot.on_message(filters.command('photo'))
def command3(bot, message):
    bot.send_photo(message.chat.id, "http://imgur.com/gallery/YUJYQ")
    bot.send_photo(message.chat.id, "https://images.app.goo.gl/6jUcGMQPxS3HKxTd7")
    bot.send_photo(message.chat.id, "https://images.app.goo.gl/149z553sqXVekdJY9")
    bot.send_photo(message.chat.id, "https://images.app.goo.gl/1qwF6ekMpvtfm9WU7")
    bot.send_photo(message.chat.id, "https://images.app.goo.gl/8S7ZW5XLshWGf1ch8")
    bot.send_photo(message.chat.id, "https://images.app.goo.gl/jVTktPxBbe9WR6kg6")
    bot.send_photo(message.chat.id, "https://images.app.goo.gl/pH9PkmxZ4geBqzoB7")
    bot.send_photo(message.chat.id, "https://images.app.goo.gl/9Eaf4h2qUKJYp1Zx9")
    bot.send_photo(message.chat.id, "https://images.app.goo.gl/u8yrjF3krwnN7Wz87")
    bot.send_photo(message.chat.id, "https://images.app.goo.gl/nxLxyaYXmn3xrxuK8")
    bot.send_photo(message.chat.id, "https://images.app.goo.gl/1mD9Rti13CQosAZXA")
    bot.send_photo(message.chat.id, "https://images.app.goo.gl/shMpXiY6hz2ARpP9A")
    bot.send_photo(message.chat.id, "https://images.app.goo.gl/i6HTzCEyCWcS5e947")
    
@bot.on_message(filters.command('bye'))
def command3(bot, message):
    bot.send_photo(message.chat.id, "https://te.legra.ph/file/c9e98feda8e73f0f5a08f.mp4")
    
@bot.on_message(filters.command('welcome'))
def command3(bot, message):
    bot.send_photo(message.chat.id, "https://te.legra.ph/file/c6a9856ae6b300813ba69.mp4")
    
@bot.on_message(filters.command('buddy'))
def command3(bot, message):
    bot.send_photo(message.chat.id, "https://te.legra.ph/file/e7b02f131aefd6140aa38.mp4")
    

@bot.on_message(filters.text)
def delete_text(bot, message):
    word_list = ["bro", "wtf", "balla", "utta", "WTF"]
    if message.text in word_list:
        bot.delete_messages(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Blocklisted word")

@bot.on_message(filters.command('leave') & filters.group)
def leave(bot, message):
    bot.send_message(message.chat.id, "Bye! I am leaving this chat.")
    bot.leave_chat(message.chat.id)

#Ban user forever
@bot.on_message(filters.command('ban') & filters.group)
def ban(bot, message):
    bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Banned!")

@bot.on_message(filters.command("stats") & filters.user(SUDO))
def botstats(_, message):
    users =len(list(all_users()))
    groups = all_groups()
    message.reply_text(f"""
Users - {users}
Groups - {groups}
    """)

@bot.on_message(filters.command("broadcast") & filters.user(SUDO))
def broadcastmsg(_, message):
    if not message.reply_to_message :
        message.reply_text("Reply to message to broadcast.")
        return
    message.reply_text("Started")                                  
    success = 0
    for user in all_users():
      try:
        userid = int(user["user_id"])
        message.reply_to_message.copy(userid)
        success += 1
      except Exception: pass
    message.reply_text(f"Broadcast Completed\nSuccess  - {success}")


print("I AM ALIVE")
bot.run()

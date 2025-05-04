class shortcuts:
    def __init__(self, event):
        self.event = event
        self.id = event.id
        self.uid = event.sender_id
        self.text = event.text or ""
        self.raw_text = getattr(event.message, 'raw_text', "")
        self.chat_id = event.chat_id
        self.chat = event.chat
        self.sender = event.sender
        self.message = event.message
        self.is_group = event.is_group
        self.is_private = event.is_private
        self.input_chat = event.input_chat
        self.reply_msg_id = event.message.reply_to_msg_id if event.message and event.message.reply_to else None
        self.buttons = event.message.buttons if event.message else None
        self.file = event.message.file if event.message and event.message.media else None
        self.media = event.message.media if event.message else None
        self.is_reply = bool(event.message.reply_to) if event.message else False
        self.fwd_from = event.message.fwd_from if event.message else None
        self.entities = event.message.entities if event.message else None
        self.mentions = event.message.get_entities_text() if event.message else None

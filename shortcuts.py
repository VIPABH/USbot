class shortcuts:
    def __init__(self, event):
        self.event = event
        self.id = event.id
        self.uid = event.sender_id
        self.text = event.text or ""
        self.chat_id = event.chat_id
        self.chat = event.chat
        self.sender = event.sender
        self.message = event.message
        self.is_group = event.is_group
        self.is_private = event.is_private

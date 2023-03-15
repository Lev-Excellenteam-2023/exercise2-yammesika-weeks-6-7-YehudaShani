class PostOffice:
    """A Post Office class. Allows users to message each other.

    Args:
        usernames (list): Users for which we should create PO Boxes.

    Attributes:
        message_id (int): Incremental id of the last message sent.
        boxes (dict): Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        Args:
            sender (str): The message sender's username.
            recipient (str): The message recipient's username.
            message_body (str): The body of the message.
            urgent (bool, optional): The urgency of the message.
                                    Urgent messages appear first.

        Returns:
            int: The message ID, auto incremented number.

        Raises:
            KeyError: If the recipient does not exist.

        Examples:
            After creating a PO box and sending a letter,
            the recipient should have 1 message in the
            inbox.

            >>> po_box = PostOffice(['a', 'b'])
            >>> message_id = po_box.send_message('a', 'b', 'Hello!')
            >>> len(po_box.boxes['b'])
            1
            >>> message_id
            1
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, user, numOfMessages=None):
        """Read a user's inbox.

        Args:
            user (str): The user whose inbox we want to read.
            numOfMessages (int): The number of messages to read.

        Returns:
            list: A list of messages.

        Raises:
            KeyError: If the user does not exist.

        Examples:
            After sending 2 messages to a user, reading the inbox
            should return a list of 2 messages.
            The inbox should be empty after reading.

            >>> po_box = PostOffice(['a', 'b'])
            >>> po_box.send_message('a', 'b', 'Hello!')
            1
            >>> po_box.send_message('a', 'b', 'Hello again!')
            2
            >>> len(po_box.read_inbox('b', 2))
            2
            >>> len(po_box.boxes['b'])
            0
        """
        user_box = self.boxes[user]
        if numOfMessages > len(user_box) or numOfMessages is None:
            result = user_box
            user_box.clear()
            return result
        else:
            result = user_box[:numOfMessages]
            del user_box[:numOfMessages]
            return result

    def search_inbox(self, user, string):
        """Search a user's inbox for a string.

        Args:
            user (str): The user whose inbox we want to search.
            string (str): The string to search for.

        Returns:
            list: A list of messages.

        Raises:
            KeyError: If the user does not exist.

        Examples:
            After sending 2 messages to a user, searching the inbox
            for a string should return a list of 1 message.

            >>> po_box = PostOffice(['a', 'b'])
            >>> po_box.send_message('a', 'b', 'Hello!')
            1
            >>> po_box.send_message('a', 'b', 'Hello again!')
            2
            >>> len(po_box.search_inbox('b', 'again'))
            1
            >>> len(po_box.search_inbox('b', 'Hello'))
            2
        """
        user_box = self.boxes[user]
        result = [message for message in user_box if string in message['body']]
        return result

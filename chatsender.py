from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio

# Replace with your own values
api_id = 25434530
api_hash = '0886a7fe39e7a2aa2b1566e58d2a1e27'
source_chat = -1002161870573  # Replace with your source chat ID
destination_chat = -1002219414457  # Replace with your destination chat ID
session_name = 'mysession'
string_session = '1BVtsOL0Bu7zfgJNkCzTV2k9r5tQLaab3_w7uCGNkt2ssizrlaBFBjd5hHpcbKkOdB3zRUNgU4Sro1u773WL4cAuk2-A_1-7Yqj5AgsfJruB0Baglrz0KuIGva90zdCpwFwkbGqv3dSuYMdt5R3YAC1i0x6sXvhAYFsbk_QBFhlnwMt3tF7iX5O7cHQ3XDM4F6E57NS3emUl4HtygWJ8LuxTGaji56XUDepIWs-i9uyhFp6C71kFHjh16H-daQeeWCTbzjkjFF-7qbO7EbpihK1CyupRD5-OqWd2dRSshqpBrPI3e4ssEouNLaieXCd8QRChzyI-6ayIMFAfcBaG6bEZMHezIakw='

client = TelegramClient(StringSession(string_session), api_id, api_hash)

async def forward_messages():
    async with client:
        # Forward messages from source_chat to destination_chat
        @client.on(events.NewMessage(chats=[source_chat]))
        async def handler(event):
            message = event.message
            print(f"Received message in source chat: {message.id} | From: {message.sender_id} | Date: {message.date} | Message: {message.text}")
            
            # Forward the message to destination_chat
            await client.forward_messages(destination_chat, message)

        print("Listening for new messages...")
        await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(forward_messages())
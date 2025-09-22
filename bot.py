import asyncio
import os
import telethonpatch  # Must import before creating client
from telethon import TelegramClient, events

# بيانات حسابك الشخصي
api_id = int(os.environ.get('TELEGRAM_API_ID', '21943267'))
api_hash = os.environ.get('TELEGRAM_API_HASH', 'd120be656f0dbe54a4ed369e70c2319b')
phone = os.environ.get('TELEGRAM_PHONE', '+201014367365')

# اسم القناة - use channel ID instead of username for reliability
channel_username = os.environ.get('TELEGRAM_CHANNEL', '-1001672479948')  # ID of 1Xbet Scripts channel

client = TelegramClient('session', api_id, api_hash)

welcome_msg = "السلام عليكم 👋\nجاهز تبدأ تشتغل معانا وتعمل فلوس؟ 💰"

# Handle pending join requests using core Telethon API
@client.on(events.Raw())
async def handle_pending_requests(event):
    """Handle join requests using UpdatePendingJoinRequests"""
    try:
        event_type = type(event).__name__
        
        # Check for pending join requests
        if event_type == 'UpdatePendingJoinRequests':
            print(f"🔍 Detected pending join requests!")
            print(f"📊 عدد الطلبات المعلقة: {event.requests_pending}")
            
            # Get the channel entity
            entity = await client.get_entity(channel_username)
            
            # Approve all pending requests
            from telethon.tl.functions.messages import HideAllChatJoinRequestsRequest
            
            result = await client(HideAllChatJoinRequestsRequest(
                peer=entity,
                approved=True  # True = approve, False = decline
            ))
            
            print(f"✅ تمت الموافقة على جميع الطلبات المعلقة!")
            
            # Send welcome messages to the requesters
            if hasattr(event, 'recent_requesters') and event.recent_requesters:
                for user_id in event.recent_requesters:
                    try:
                        # First get the user entity to ensure we can send messages
                        user_entity = await client.get_entity(user_id)
                        await client.send_message(user_entity, welcome_msg)
                        print(f"💬 تم إرسال رسالة الترحيب للعضو {user_entity.first_name} ({user_id})")
                    except Exception as msg_error:
                        print(f"❌ خطأ في إرسال الرسالة للعضو {user_id}: {msg_error}")
                        # Alternative: Try sending via user ID as string
                        try:
                            await client.send_message(int(user_id), welcome_msg)
                            print(f"💬 تم إرسال رسالة الترحيب للعضو {user_id} (backup method)")
                        except Exception as backup_error:
                            print(f"❌ فشل الإرسال نهائياً للعضو {user_id}: {backup_error}")
                        
    except Exception as e:
        print(f"❌ خطأ في معالجة الطلبات: {e}")

# Backup handler for chat actions
@client.on(events.ChatAction(chats=channel_username))
async def handle_chat_action(event):
    """Monitor chat actions for debugging"""
    print(f"🔄 Chat action in {channel_username}:")
    if event.user_joined:
        print("👤 User joined")
        # Send welcome message to newly joined user
        try:
            user = await event.get_user()
            await client.send_message(user.id, welcome_msg)
            print(f"💬 تم إرسال رسالة الترحيب للعضو الجديد {user.id}")
        except Exception as e:
            print(f"❌ خطأ في الترحيب: {e}")
    if event.user_added:
        print("➕ User added")
    if event.user_left:
        print("👋 User left")
    if event.user_kicked:
        print("🚫 User kicked")

async def main():
    await client.start(phone)
    print("🚀 Userbot started successfully!")
    
    # List all chats to find the target channel
    print("🔍 البحث عن القنوات المتاحة...")
    target_entity = None
    
    async for dialog in client.iter_dialogs():
        if dialog.is_channel:
            print(f"📺 قناة: {dialog.title} - ID: {dialog.id}")
            if "1xbet" in dialog.title.lower() or "scripts" in dialog.title.lower():
                target_entity = dialog.entity
                print(f"✅ تم العثور على القناة المطلوبة: {dialog.title}")
                break
    
    if not target_entity:
        print("❌ لم يتم العثور على القناة المطلوبة")
        print("📝 أرسل لي username القناة الصحيح")
        return
    
    # Update the global channel reference
    global channel_username
    channel_username = target_entity
    
    # Check permissions
    try:
        permissions = await client.get_permissions(target_entity, 'me')
        print(f"🔑 الصلاحيات: Admin = {permissions.is_admin}, Can invite = {permissions.invite_users}")
    except Exception as e:
        print(f"❌ خطأ في التحقق من الصلاحيات: {e}")
    
    print("👂 البوت يستمع لطلبات الانضمام...")
    await client.run_until_disconnected()

asyncio.run(main())

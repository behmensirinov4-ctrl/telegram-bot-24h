import os
import requests
from datetime import datetime

TOKEN = os.getenv('8242695032:AAHmNJvIAxnBnuZDOMDUVjQhwS7QLJRX7kc')
CHAT_ID = os.getenv('-1002151723621')

def main():
    print("🤖 GitHub Bot Başladı...")
    
    try:
        message = f"""🤖 GitHub Actions Bot
        
✅ Bot aktivdir
⏰ {datetime.now().strftime('%H:%M:%S')}
📅 {datetime.now().strftime('%Y-%m-%d')}
📍 GitHub Server
🔄 Hər 3 dəqiqədə"""
        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message}
        
        response = requests.post(url, json=data, timeout=10)
        
        if response.status_code == 200:
            print("✅ Mesaj göndərildi!")
        else:
            print(f"❌ Xəta: {response.text}")
            
    except Exception as e:
        print(f"❌ Bağlantı: {e}")

if __name__ == "__main__":
    main()

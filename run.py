from dotenv import load_dotenv
import os

print("🟢 Seeder Server Booting...")

load_dotenv()

creator_id = os.getenv("CREATOR_ID")
auth_token = os.getenv("AUTH_TOKEN")
mode = os.getenv("MODE")

def main():
    print("Creator ID:", creator_id)
    print("Auth Token:", auth_token)
    print("Mode:", mode)
    print("🚀 Server is running...")

if __name__ == "__main__":
    main()
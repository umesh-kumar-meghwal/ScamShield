import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("https://pabknuafhuozdylipmzf.supabase.co")
SUPABASE_KEY = os.getenv("sb_publishable_EMeBKRjWMn0gJM1p0-DxNw_hwhbS4XX")

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)
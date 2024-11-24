from dotenv import load_dotenv, find_dotenv
import os

# 加载环境变量
load_dotenv(find_dotenv())

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    # DATABASE_URL = os.getenv("DATABASE_URL", "data/real_estate.db")
    #GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "your_google_maps_api_key")
    #LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

app = FastAPI(title="Supabase FastAPI App")

# Supabase 設定
URL: str = os.getenv("SUPABASE_URL")
KEY: str = os.getenv("SUPABASE_SERVICE_ROLE_KEY") # 後端使用 Service Role Key 以跳過 RLS
supabase: Client = create_client(URL, KEY)

# 定義資料格式
class NumberInput(BaseModel):
    value: int

# 靜電檔案掛載
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    return FileResponse("static/index.html")

@app.get("/admin", response_class=HTMLResponse)
async def read_admin():
    return FileResponse("static/admin.html")

# API: 寫入數字
@app.post("/api/numbers")
async def add_number(item: NumberInput):
    try:
        response = supabase.table("numbers").insert({"value": item.value}).execute()
        return {"status": "success", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# API: 讀取最新 50 筆
@app.get("/api/numbers")
async def get_numbers():
    try:
        response = supabase.table("numbers").select("*").order("created_at", desc=True).limit(50).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

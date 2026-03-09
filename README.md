# FastAPI + Supabase Web App (Render 部署版)

這是一個簡單的 Web 應用程序，具備數字輸入頁面與即時更新的後台管理頁面。

## 目錄結構
- `app/main.py`: 後端 API (FastAPI)
- `static/`: 前端網頁
- `sql/init.sql`: 資料庫建表 SQL
- `render.yaml`: Render 雲端部署設定

## 本機執行步驟
1. 安裝 Python 3.9+
2. 安裝依賴: `pip install -r requirements.txt`
3. 複製並設定環境變數: `cp .env.example .env` (並填入您的 Supabase 資訊)
4. 啟動伺服器: `python app/main.py`
5. 開啟瀏覽器: `http://localhost:8000`

## Supabase 設定步驟
1. 在 Supabase 建立專案。
2. 在 SQL Editor 執行 `sql/init.sql` 中的內容。
3. **重要**: 前往 `Database` -> `Replication` -> `Publications` -> `supabase_realtime`，確保 `numbers` 表格已勾選 `Insert`。
4. 獲取 `URL`、`Anon Key` 與 `Service Role Key`。

## Render 部署步驟
1. 將程式碼推送到 GitHub。
2. 在 Render 選擇 `New` -> `Blueprints`，連結此 Repo。
3. 或手動建立 `Web Service`。
4. 設定以下環境變數 (Environment Variables):
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`
   - `SUPABASE_SERVICE_ROLE_KEY`
   - `PYTHON_VERSION`: 3.9 或更高

## 實作說明
- **即時更新**: 採用 Supabase Realtime (JS SDK)。
- **安全性**: 後端使用 Service Role Key 進行操作，避免 RLS 權限問題；前端僅使用 Anon Key 進行 Realtime 監聽。
- **後台保護**: 目前為簡化版，無登入驗證。

## 未來建議補強
- 加入用戶認證 (Supabase Auth)。
- 增加更多的資料欄位與篩選功能。
- 優化 RLS (Row Level Security) 政策。

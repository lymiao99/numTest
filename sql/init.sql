-- 建表 SQL
CREATE TABLE IF NOT EXISTS public.numbers (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    value INTEGER NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 啟用 Realtime (如果尚未啟用)
-- 注意: 您需要在 Supabase Dashboard -> Realtime 設定中勾選 numbers 表格的 Insert/Update/Delete
-- 或者執行以下指令 (視權限而定):
-- ALTER PUBLICATION supabase_realtime ADD TABLE numbers;

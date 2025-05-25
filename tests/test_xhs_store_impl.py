import sys
import os
import csv
import shutil
import pathlib
import asyncio
import pytest

# 确保可以导入 store 包
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from store.xhs.xhs_store_impl import XhsCsvStoreImplement


@pytest.mark.asyncio
async def test_save_data_to_csv_simple():
    test_dir = "data/xhs/test_save"
    os.makedirs(test_dir, exist_ok=True)

    class TestStore(XhsCsvStoreImplement):
        csv_store_path = test_dir
        file_count = 1

    store = TestStore()
    save_item = {"id": "123", "title": "测试标题", "count": 42}

    await store.save_data_to_csv(save_item, store_type="contents")

    files = list(pathlib.Path(test_dir).glob("*.csv"))
    assert files, "CSV 文件未创建"

    with open(files[0], encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows[0] == list(save_item.keys())
        assert rows[1] == [str(v) for v in save_item.values()]

    shutil.rmtree(test_dir)

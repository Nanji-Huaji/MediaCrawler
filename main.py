# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：
# 1. 不得用于任何商业用途。
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。
# 3. 不得进行大规模爬取或对平台造成运营干扰。
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。
# 5. 不得用于任何非法或不当的用途。
#
# 详细许可条款请参阅项目根目录下的LICENSE文件。
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。


import asyncio
import sys

import json

import cmd_arg
import config
import db
from base.base_crawler import AbstractCrawler
from media_platform.bilibili import BilibiliCrawler
from media_platform.douyin import DouYinCrawler
from media_platform.kuaishou import KuaishouCrawler
from media_platform.tieba import TieBaCrawler
from media_platform.weibo import WeiboCrawler
from media_platform.xhs import XiaoHongShuCrawler
from media_platform.zhihu import ZhihuCrawler
import store.xhs.xhs_store_impl
import store.weibo.weibo_store_impl
import store.tieba.tieba_store_impl


class ReturnCSVFileFactory:
    MAKE_SAVE_FILE_NAME = {
        "xhs": store.xhs.xhs_store_impl,
        "weibo": store.weibo.weibo_store_impl,
        "tieba": store.tieba.tieba_store_impl,
    }

    @staticmethod
    def get_csv_name_func(platform: str):
        """
        获取指定平台的文件命名函数

        Args:
            platform: 平台名称 (xhs, wb, tieba等)

        Returns:
            对应平台的make_save_file_name函数
        """
        store_module = ReturnCSVFileFactory.MAKE_SAVE_FILE_NAME.get(platform)
        if not store_module:
            raise ValueError(f"不支持的平台: {platform}")

        # 获取对应平台的CsvStoreImplement类
        csv_store_class = getattr(store_module, f"{platform.capitalize()}CsvStoreImplement", None)
        if not csv_store_class:
            raise ValueError(f"找不到{platform}的CSV存储实现类")

        # 创建类实例并返回其make_save_file_name方法
        instance = csv_store_class()
        return instance.make_save_file_name


class CrawlerFactory:
    CRAWLERS = {
        "xhs": XiaoHongShuCrawler,
        "dy": DouYinCrawler,
        "ks": KuaishouCrawler,
        "bili": BilibiliCrawler,
        "wb": WeiboCrawler,
        "tieba": TieBaCrawler,
        "zhihu": ZhihuCrawler,
    }

    @staticmethod
    def create_crawler(platform: str) -> AbstractCrawler:
        crawler_class = CrawlerFactory.CRAWLERS.get(platform)
        if not crawler_class:
            raise ValueError("Invalid Media Platform Currently only supported xhs or dy or ks or bili ...")
        return crawler_class()


async def main():
    # parse cmd
    await cmd_arg.parse_cmd()

    # init db
    if config.SAVE_DATA_OPTION == "db":
        await db.init_db()

    crawler = CrawlerFactory.create_crawler(platform=config.PLATFORM)
    await crawler.start()

    if config.SAVE_DATA_OPTION == "db":
        await db.close()


def run_main() -> None | dict:
    try:
        # asyncio.run(main())
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        sys.exit()
    if config.SAVE_DATA_OPTION == "csv":
        make_save_file_func = ReturnCSVFileFactory.get_csv_name_func(config.PLATFORM)
        return {
            "comment": make_save_file_func("comment"),
            "content": make_save_file_func("content"),
            "creater": make_save_file_func("creater"),
        }


if __name__ == "main":
    RESULT_PREFIX = "@@RESULT@@ "
    ret = run_main()
    if ret is not None:
        print(RESULT_PREFIX + json.dumps(ret, ensure_ascii=False))

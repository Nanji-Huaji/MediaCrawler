import os
import asyncio
import csv
import shutil
import pathlib
import pytest
from store.xhs.xhs_store_impl import XhsCsvStoreImplement

import sys


@pytest.mark.asyncio
async def test_save_data_to_csv():
    # 设置测试目录，避免污染正式数据
    test_dir = "data/xhs/test_save"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.makedirs(test_dir, exist_ok=True)

    # 构造测试实例和参数
    class TestStore(XhsCsvStoreImplement):
        csv_store_path = test_dir
        file_count = 1

    store = TestStore()
    save_item = {
        "items": [
            {
                "id": "65afc71b000000000c0072a0",
                "model_type": "note",
                "note_card": {
                    "image_list": [
                        {"height": 2560, "width": 1920},
                        {"height": 1379, "width": 1420},
                        {"height": 1365, "width": 609},
                    ],
                    "corner_tag_info": [{"type": "publish_time", "text": "2024-01-23"}],
                    "type": "normal",
                    "display_title": "一小时赚1600，转码依然是出路",
                    "user": {
                        "nickname": "nightlight",
                        "xsec_token": "ABsgDYfbSBZkvkQ8OjaZ5404nqzIFascHLQc5013uBrkc=",
                        "nick_name": "nightlight",
                        "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/5a054105b46c5d3a124021a2.jpg?imageView2/2/w/80/format/jpg",
                        "user_id": "5a05410311be105800850be0",
                    },
                    "interact_info": {
                        "liked": False,
                        "liked_count": "4311",
                        "collected": False,
                        "collected_count": "3551",
                        "comment_count": "514",
                        "shared_count": "1147",
                    },
                    "cover": {"height": 2560, "width": 1920},
                },
                "xsec_token": "ABvqqgagt-yzvwzRBsZ2GJSLXHc6dgE3CJcTgsYwMHJKA=",
            },
            {
                "id": "5f6739b1000000000100550f",
                "model_type": "note",
                "note_card": {
                    "cover": {"height": 1322, "width": 992},
                    "image_list": [{"height": 1322, "width": 992}],
                    "corner_tag_info": [{"type": "publish_time", "text": "2020-09-20"}],
                    "type": "normal",
                    "display_title": "适合做副业赚钱的10个方法，给你总结好",
                    "user": {
                        "nick_name": "星野",
                        "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/53ba1722242c3e9344db7b0fc2e1005f.jpg?imageView2/2/w/80/format/jpg",
                        "user_id": "5f12642600000000010007c1",
                        "nickname": "星野",
                        "xsec_token": "AB6K7x0JubTFLTfF8HRzcurfQW_Fun5OWRBeC9p6IyAe0=",
                    },
                    "interact_info": {
                        "liked": False,
                        "liked_count": "2798",
                        "collected": False,
                        "collected_count": "2209",
                        "comment_count": "126",
                        "shared_count": "92",
                    },
                },
                "xsec_token": "ABYyzYj9NYGxNowZ43usbxk0BgBo_5dhWyooitWLyAz8c=",
            },
            {
                "id": "666aadb3000000001d01bccc",
                "model_type": "note",
                "note_card": {
                    "display_title": "用python技能去变现，实现经济自由",
                    "user": {
                        "nick_name": "vitality",
                        "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo313cf152cg45g5o7jphc08lihvj71ruo?imageView2/2/w/80/format/jpg",
                        "user_id": "60f3cc580000000001005651",
                        "nickname": "vitality",
                        "xsec_token": "AB92Okop3LGbPNNNza5zgBspiYRkcB4k0Xoam9T8SRchU=",
                    },
                    "interact_info": {
                        "shared_count": "233",
                        "liked": False,
                        "liked_count": "2050",
                        "collected": False,
                        "collected_count": "2314",
                        "comment_count": "69",
                    },
                    "cover": {"height": 2560, "width": 1937},
                    "image_list": [
                        {"height": 2560, "width": 1937},
                        {"height": 2560, "width": 1942},
                        {"height": 1756, "width": 2560},
                    ],
                    "corner_tag_info": [{"text": "2024-06-13", "type": "publish_time"}],
                    "type": "normal",
                },
                "xsec_token": "ABUpO690KtP0a_ni6kvMtoCVSaMLxDLYb2N-HdukEhHYw=",
            },
            {
                "id": "67d8f14d000000001d01f16b",
                "model_type": "note",
                "note_card": {
                    "interact_info": {
                        "comment_count": "211",
                        "shared_count": "734",
                        "liked": False,
                        "liked_count": "2007",
                        "collected": False,
                        "collected_count": "3217",
                    },
                    "cover": {"height": 1660, "width": 1245},
                    "image_list": [
                        {"width": 1245, "height": 1660},
                        {"height": 1660, "width": 1245},
                        {"height": 1660, "width": 1245},
                        {"height": 1660, "width": 1245},
                        {"height": 1660, "width": 1245},
                        {"height": 1660, "width": 1245},
                        {"height": 1660, "width": 1245},
                        {"height": 1660, "width": 1245},
                        {"height": 1660, "width": 1245},
                        {"height": 1660, "width": 1245},
                        {"width": 1245, "height": 1660},
                        {"height": 1660, "width": 1245},
                        {"width": 1245, "height": 1660},
                        {"height": 1660, "width": 1245},
                        {"height": 1660, "width": 1245},
                    ],
                    "corner_tag_info": [{"type": "publish_time", "text": "03-18"}],
                    "type": "normal",
                    "display_title": "2025程序员赚米兼职平台（大汇总）",
                    "user": {
                        "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/63c7675afe300552c7be3e3f.jpg?imageView2/2/w/80/format/jpg",
                        "user_id": "5dc69dbe0000000001004ac0",
                        "nickname": "程序员鱼皮",
                        "xsec_token": "ABBBWoegb1byQIdwsYBKTdtV11tfEsJo7HMnlmRgCqOss=",
                        "nick_name": "程序员鱼皮",
                    },
                },
                "xsec_token": "ABUqGM2MyvIBqNFWZeQOUD23yDqdEvjP0DL1eiO_y4-g8=",
            },
            {
                "model_type": "note",
                "note_card": {
                    "type": "normal",
                    "display_title": "🇲🇾 7种种低门槛创业机会  普通人请进 💻📱",
                    "user": {
                        "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/65154cc8728d4fda5b19d85f.jpg?imageView2/2/w/80/format/jpg",
                        "user_id": "64faeed10000000004027956",
                        "nickname": "肉包zi",
                        "xsec_token": "ABrvBF6TpxDodCiPtE36jrFl7uYbp3zcY2tAD1FE1fW8s=",
                        "nick_name": "肉包zi",
                    },
                    "interact_info": {
                        "liked_count": "1856",
                        "collected": False,
                        "collected_count": "2083",
                        "comment_count": "378",
                        "shared_count": "55",
                        "liked": False,
                    },
                    "cover": {"height": 1920, "width": 1440},
                    "image_list": [{"height": 1920, "width": 1440}],
                    "corner_tag_info": [{"type": "publish_time", "text": "2023-10-16"}],
                },
                "xsec_token": "ABzqHna1oHfTpl-PVKe5oYHLbfiQz3iG29fUVCpM4mx8M=",
                "id": "651ceab3000000001e0286f6",
            },
            {
                "id": "65bd07cb000000002d00135a",
                "model_type": "note",
                "note_card": {
                    "display_title": "学习python的第一桶金！",
                    "user": {
                        "nick_name": "莫念",
                        "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/5eb151b00000000001007de4.jpg?imageView2/2/w/80/format/jpg",
                        "user_id": "5eb151b00000000001007de4",
                        "nickname": "莫念",
                        "xsec_token": "ABkOYyK24-yVz5dFsLxES1sNo4UAX0Zmdl7-cJgTxR0KE=",
                    },
                    "interact_info": {
                        "liked": False,
                        "liked_count": "1727",
                        "collected": False,
                        "collected_count": "1630",
                        "comment_count": "152",
                        "shared_count": "69",
                    },
                    "cover": {"width": 2363, "height": 2560},
                    "image_list": [{"height": 2560, "width": 2363}],
                    "corner_tag_info": [{"type": "publish_time", "text": "2024-02-02"}],
                    "type": "normal",
                },
                "xsec_token": "ABbxCzbDh6bSAOEsjHsxZ6EViM2cjugcKboUfGhrY-nk0=",
            },
            {
                "id": "6790b3eb000000001902d203",
                "model_type": "note",
                "note_card": {
                    "corner_tag_info": [{"type": "publish_time", "text": "01-25"}],
                    "type": "normal",
                    "display_title": "程序员接私活，一小时赚300，放假也不敢休息",
                    "user": {
                        "nick_name": "深漂程序员犬夜叉",
                        "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/6460f653f9ef96cf85921fb1.jpg?imageView2/2/w/80/format/jpg",
                        "user_id": "634cbadf000000001901d06e",
                        "nickname": "深漂程序员犬夜叉",
                        "xsec_token": "ABOcASNPtOz9_B3sJKxwXTd5vyno_Lv7QqRKdN5yQEBew=",
                    },
                    "interact_info": {
                        "shared_count": "219",
                        "liked": False,
                        "liked_count": "1329",
                        "collected": False,
                        "collected_count": "436",
                        "comment_count": "601",
                    },
                    "cover": {"height": 4032, "width": 3024},
                    "image_list": [
                        {"height": 4032, "width": 3024},
                        {"height": 4032, "width": 3024},
                        {"width": 3024, "height": 4032},
                        {"height": 1406, "width": 1013},
                    ],
                },
                "xsec_token": "ABTJzTnWbcLoWK0wiUKdjnXldoBVp-dUiad5DKis1cMS0=",
            },
            {
                "id": "67a1bab7000000001902fce0",
                "model_type": "note",
                "note_card": {
                    "cover": {"height": 2560, "width": 1920},
                    "image_list": [
                        {"height": 2560, "width": 1920},
                        {"height": 2560, "width": 1920},
                        {"height": 2560, "width": 1920},
                    ],
                    "corner_tag_info": [{"type": "publish_time", "text": "02-05"}],
                    "type": "normal",
                    "display_title": " 程序员接私活，用ai写程序，4小时赚2500",
                    "user": {
                        "nick_name": "深漂程序员犬夜叉",
                        "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/6460f653f9ef96cf85921fb1.jpg?imageView2/2/w/80/format/jpg",
                        "user_id": "634cbadf000000001901d06e",
                        "nickname": "深 漂程序员犬夜叉",
                        "xsec_token": "ABOcASNPtOz9_B3sJKxwXTd5vyno_Lv7QqRKdN5yQEBew=",
                    },
                    "interact_info": {
                        "liked_count": "879",
                        "collected": False,
                        "collected_count": "474",
                        "comment_count": "220",
                        "shared_count": "248",
                        "liked": False,
                    },
                },
                "xsec_token": "ABoe0eO6MKf45KEGUTbdnlZA8r9h4p8up4rljhPtY4dnI=",
            },
            {
                "model_type": "note",
                "note_card": {
                    "corner_tag_info": [{"type": "publish_time", "text": "03-13"}],
                    "type": "normal",
                    "user": {
                        "xsec_token": "AB4j1Ciq132pQv3ywwiVQeDoULN_7ZHkBIOLt7DR2uA90=",
                        "nick_name": "甜果儿🍅",
                        "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo31eo0u84166405o8vn7m08308u2ctgd0?imageView2/2/w/80/format/jpg",
                        "user_id": "611fb9ec0000000001000c08",
                        "nickname": "甜果儿🍅",
                    },
                    "interact_info": {
                        "liked_count": "876",
                        "collected": False,
                        "collected_count": "245",
                        "comment_count": "2815",
                        "shared_count": "62",
                        "liked": False,
                    },
                    "cover": {"height": 2560, "width": 1931},
                    "image_list": [{"height": 2560, "width": 1931}],
                },
                "xsec_token": "AB4t0rp4eM4okGo5pVCUXG3PB8ASZabeF7s9yJAYyl36w=",
                "id": "67d24db7000000000900d19f",
            },
            {
                "id": "663a366d000000001e021d92",
                "model_type": "note",
                "note_card": {
                    "image_list": [{"height": 1600, "width": 1200}],
                    "corner_tag_info": [{"type": "publish_time", "text": "2024-05-07"}],
                    "type": "normal",
                    "display_title": "\U0001f979听我一句劝：程序员接私单就是扯淡\U0001f979",
                    "user": {
                        "nickname": "退役程序员锋哥",
                        "xsec_token": "ABnJfzXBtyvNgh-s_2LTMR3T2eius5DPuKEU2I87Q5DZQ=",
                        "nick_name": "退役程序员锋哥",
                        "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/6566e291f87da4b4bd8e3958.jpg?imageView2/2/w/80/format/jpg",
                        "user_id": "5819ff4f5e87e779a1fa99dd",
                    },
                    "interact_info": {
                        "collected_count": "706",
                        "comment_count": "553",
                        "shared_count": "229",
                        "liked": False,
                        "liked_count": "601",
                        "collected": False,
                    },
                    "cover": {"height": 1600, "width": 1200},
                },
                "xsec_token": "ABXsautH0uPsytw_Tl2j99WlG1-0RGmZcWhKUhF1aawBo=",
            },
        ]
    }

    # 执行保存
    await store.save_data_to_csv(save_item, store_type="contents")

    # 检查文件是否创建
    files = list(pathlib.Path(test_dir).glob("*.csv"))
    assert files, "CSV 文件未创建"
    # 检查内容
    with open(files[0], encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert rows[0] == list(save_item.keys())
        assert rows[1] == [str(v) for v in save_item.values()]
    print("Test completed successfully, CSV file created and verified.")
    # 清理
    # shutil.rmtree(test_dir)

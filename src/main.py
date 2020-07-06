#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from config import ASSET
# import scenes
from scenes import stage


################################################################
#
#   1. Story memo
#   2. Story structure
#   3. Plot
#   4. Conte
#   5. Draft
#
################################################################

# Constant
TITLE = "本を喰む子"
ONELINE = "本屋の店主から、本を食べてしまうという子の話を聞く"
OUTLINE = "約6000字のホラー短編。よく利用している本屋である日、あなたは店主から奇妙な子どもの話を聞かされるが"
MAJOR, MINOR, MICRO = 1, 3, 1


# Episodes
def ep1(w: World):
    return w.episode('本を読む人',
            stage.sc_read_book(w),
            )

def ep2(w: World):
    return w.episode('本を喰む子',
            stage.sc_eat_book(w),
            )

def ep3(w: World):
    return w.episode('本が消える音',
            stage.sc_vanish_book(w),
            )

def ch_main(w: World):
    return w.chapter('main',
            ep1(w),
            ep2(w),
            ep3(w),
            w.symbol("（了）"),
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(ASSET)
    w.config.set_contest_info("エブリスタの妄想コンテスト「一冊の本」優秀作に選出")
    w.config.set_caution("本作はホラーですので、耐性のない方は読まないことをおすすめします")
    w.config.set_sites("エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム")
    w.config.set_released(11, 27, 2018)
    return w.run(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())


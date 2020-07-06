# -*- cofing: utf-8 -*-
'''
Stage: xxx
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def sc_read_book(w: World):
    who = w.get("who")
    return w.scene("本を読む人",
            who.do("すれ違うには背中合わせにならないと無理だな、と｜あなた《・・・》は本棚に囲まれて感じる"),
            who.do("何年も置かれたままの本たちだからか、紙とインクの匂いというよりやや黴臭《かびくさ》いようなそれを感じつつ、あなたは思いの一冊に人差し指を当てた。その黒っぽい背表紙の一冊を、タイトルと番号を確かめてから引き抜く", "&"),
            who.do("分厚い文庫本だ。八十年ほど前に亡くなった米国の作家の全集だが、今でも多くの人により読み継がれている作品群がここに眠っている。あなたはそこに挟まれたスリップと呼ばれる書名等が記載された二つ折りの紙を抜き、ページを開く"),
            who.do("文章は難解だ。翻訳ということを置いてもエッセイを読むようには進まない", '&'),
            who.do("それでも一つ一つの表現から浮かび上がる世界はあなたを虜《とりこ》にしていた"),
            who.do("ただ、ずっと没頭していられるかと言えばそうでもなく、あなたはそっと奥のカウンターに座る白髪を乱雑に後ろでまとめた店主の様子を覗《のぞ》き見やる。眼鏡の位置を調整し、指の先が切られたグレィの手袋で、重そうなハードカバーを読んでいた。昨日とは違う色だから新しい本に取り掛かったようだ"),
            who.do("立ち読みをしていて彼女に何か言われたことはない"),
            who.do("歴史が染み付いたような黒ずんだ本棚は、上の方に埃《ほこり》が見える。店内がやや暗くなっているのも節電というより蛍光灯を替えていない為だ。一つは完全に消えてしまっている"),
            who.do("できればこの全集を読み終えるまでは、と、あなたは心の中で手を合わせる"),
            who.do("それから十五分、いや三十分程度だろうか、再び本にスリップを挟むと、見つからないようにそっと棚に戻した。順番も並ぶ高さもぴたりと揃える"),
            who.do("――また明日"),
            who.do("そう微笑し、あなたは店を出た"),
            w.br(),
            who.do("雲の多い天気に気を悪くしながらも、翌日も鳳書店《おおとりしょてん》の木戸を開ける"),
            who.do("海外小説の翻訳版は向かって右手の真ん中の通路脇の一画に並べられていて、あなたは一応客の振りで一番左手の通路を奥まで歩いてから、きょろきょろと探している視線を使い、一瞬それで店主を確認する"),
            who.do("今日も彼女は本を読んでいた"),
            who.do("年齢は分からない。ただずっと同じ姿形、それに殆《ほとん》ど変わらない服装なので、妖怪なのかも知れない、と内心で笑う"),
            who.do("所定の位置までやってきてから再度カウンターを見やると、店主は丁寧にページを捲《めく》っているところだった。時折溜息をつく。どんな本を読んでいるのか気になったが、それよりも自分が見ている物語の続きが気になり、本棚に視線を戻した"),
            who.do("黒い背表紙の全集、その三巻目に手を伸ばす。栞《しおり》代わりに挟んでおいたスリップを抜いてから、気づいた。一巻目の左隣に空間ができている。本が売れたのだろう。同じ著者の別の作品だったが、それでも自分以外にこの本屋に立ち寄り、誰かが購入していった、ということに驚きを感じた"),
            who.do("でも大丈夫だろう、と根拠のない安心を言い聞かせ、あなたは続きを読み耽《ふけ》った"),
            w.br(),
            who.do("しかし翌日、更にその次の日も、本は消えていた。同じ著者の別の作品だけでなく、遂に今日はあなたが読んでいる本の二つ前の文庫も、消えてしまった"),
            who.do("まだ、半分も読んでいないのに"),
            who.do("難解な報告書のような著作を、誰が好んで買っていくのだろう", '&'),
            who.do("もう一人の自分がいるのだろうか", '&'),
            who.do("読んでいる小説の影響か、そんなホラーを考えてしまう"),
            w.br(),
            who.do("その日は酷い雨だった。傘を畳み、軒下の錆《さ》び付いた金属の格子にそれを立て、店に入る"),
            who.do("ちょうど入り口の真上の蛍光灯が何度か閃《ひらめ》いた。もう寿命だろう。それでも交換をしないというのは、あの老婆の目がそれほど明かりを気にしないということかも知れない", '&'),
            who.do("あなたはさっさと海外小説の棚に行き、自分の本を手に取る。全集の三巻目を探す"),
            who.do("ない"),
            who.do("三巻目だけでなく、七冊あるうちの最後の一巻を除いた全ての本が棚から消えていた"),
            who.do("――嘘だ"),
            who.do("心の中で何度も言い、あなたはもう一度確かめる。誰かが別の場所に間違って仕舞ったのではないか。それとも棚そのものを間違えたのだろうか。何度も確かめた。だが自分の本が消えてしまっているという事実を確認するだけだった"),
            who.do("早鐘が打つ"),
            who.do("あなたは落ち着こうと第七巻に手を伸ばして、はたと思う"),
            who.do("カウンターを見た。老いた店主はじっと本を読み耽っている"),
            who.do("――大丈夫"),
            who.do("何が？"),
            who.do("――いいから。そう。何も問題はない"),
            who.do("まるで手にした本と対話しているようだった。表紙の白抜きされた著者のイラストが、あなたに微笑みかけているのだと思った"),
            who.do("鞄を開ける"),
            who.do("気づくとそこに、あなたの手から本が落ちていった"),
            who.do("蓋《ふた》を閉め、一度周囲を見回してから、足を入り口へと向ける"),
            who.do("心音なのか、靴音なのか、その聞き分けがつかない"),
            who.do("木枠のガラス戸の前まで来ると、ゆっくりと力を入れる。少し開き始めたところで、ガタン、と躓《つまず》いた。木戸が開かない。あなたは何度も揺らしてそれを開けようとする。しかし動かない。開くことも閉じることもできず、どうしようかと振り返ったところで、ぬっとグレィの手袋から出た指先が、あなたの戸を掴《つか》んだ"),
            who.talk("これ、滑りが悪くてね"),
            who.do("老婆は何度か戸を叩き、それから今一度力を入れて押しやる。木戸は全て開いてしまった"),
            who.do("あなたは小さく頭を下げ、店を出る。足を外へと踏み出す"),
            who.talk("店を出た、ということの意味を、あんたは理解しているよね？"),
            who.do("振り返ろうとしたあなたの手を、彼女の手が思いのほか強い力で握り締めていた"),
            )

def sc_eat_book(w: World):
    who = w.get("who")
    return w.scene("本をはむ子",
            who.do("あなたは店主について、店のカウンターの奥に入る"),
            who.do("段ボール箱が積み上がり、事務机にはパソコンが載っていた"),
            who.do("パイプ椅子によろよろと座り、お茶を出す老婆と膝《ひざ》を突き合わせるようになる。彼女の椅子は手すりがある回転式のものだ。その眼鏡を掛け直すと、マウスを操作してパソコンをスクリーンセーバに切り替えた"),
            who.talk("自分が何をしたのか、ということをあれこれ言うつもりはないよ。もう大人なんだ。そういう話はしなくてもいいだろう。そうだね"),
            who.do("あなたの湯呑みからは黙って湯気が立ち昇っている"),
            who.do("店主はコーヒーカップを両手で支え、その中の黒い液体を口に含んだ"),
            who.talk("ここは私の祖父の頃にはね、貸本屋だったんだよ。知ってるかね。今でもまだやってるとこがあるかも知れないけど、昔は本や雑誌をビデオのように貸し出すところがあったんだよ"),
            who.do("自分の湯呑みにそっと手を当てると、冷たくなっていた手が僅《わず》かに熱を持つ"),
            who.talk("その頃は米穀通帳《べいこくてちょう》ってのがあって。まあ身分証の代わりみたいなものだね。米軍から配給を受ける時に必要だったものさ。漫画本中心だったから、近所の子もよく通っててね"),
            who.do("もう店主はあなたを見ていなかった"),
            who.do("それは今から四十年ほど前のことだ、と彼女は前置きしてから、昔話を始めた"),
            w.symbol("　　　　※"),
            who.do("あの当時は本当に色々な子がいて、中でも朋久《ともひさ》君っていう、それこそ今で言う発達障害かね、何を考えているのか分からない男の子がいて、その子は毎日のように貸本屋に来ていた。他の子供たちは漫画を読んだり、借りていったりしたけれど、朋久君だけは難しい漢字が並ぶ小説本を何時間もじっと眺めていたんだ"),
            who.do("あれは読んでるっていうより、ただ見てたって方が合ってるね"),
            who.do("変わった子の話は、よく祖父《じい》さんから聞かされたよ。もともと道楽で貸本なんてやってる人だったから、人が善《よ》くてね。いつだったかは知らない子を勝手に家に上げて晩御飯を食べさせてやったりするような、そんな祖父さんだった"),
            who.do("まあ当時から万引きってのもあってね。それを見つけたら「こら」って一応ゲンコツしてから、"),
            who.talk("もう二度と他人のものを盗んじゃいけない"),
            who.do("と言い聞かせて、その本を子供らに与えてた"),
            who.do("何にしてもみんなが貧しい時代だったからね。ちょっとくらいのことは大目に見てやってたんだろう"),
            who.do("ところが、その朋久君がね、ある日だよ、自分が読んでいた本のページを破いて口に入れちまったんだ。祖父さんは慌てて出すように言ったんだが、頑として聞かなくて。結局そのまま呑み込んじまった"),
            who.talk("お腹が空いてるんなら、これを食え"),
            who.do("祖父さんはチョコレートをやろうとしたんだって。けど、朋久君は首を振り、また一ページ破いて食ったんだ"),
            who.do("それからは毎日一冊、彼は本を食べるようになって"),
            who.do("流石に心配になって、祖父さんは朋久君の両親に話した方がいいだろうかどうだろうかと悩んだらしいけど、何でも親が気難しい人で、一度話に行くと金を渡されてピシャっと玄関を閉められてしまったそうだよ"),
            who.do("そんなことがあってからも朋久君は変わらずに店にやってきては本を食べていくから、そのうちに棚一つ分が空いちゃってね。こりゃ敵わんってことで、うちの裏手に蔵が建ってるんだけど、そこに和綴じの古い本が大量に余ってて、どうせならそれを食べてもらおうってことで、彼に一日一冊、渡すようにしたんだ"),
            who.do("虫食いしてたり、ページが抜けてたり、売っても二束三文にしかならないからと置いてた本が、見る間に消えていったそうだよ"),
            who.do("それでもいつか止めるんじゃないだろうかって、思ってたんだろうね"),
            who.do("ところでその蔵の本の中には、一冊だけ見ることすら禁じられていた本があったんだ。その話は祖父さんからもきつく言われてたから、よく覚えてるよ。名前も分からない、そもそも表紙に書いてある文字が読めないんだって。日本語でも英語でもないみたいで、もうそんな話だから、誰も確認しようとしなかったけれど、実は私はね、一度だけ蔵に入って、それらしい黒い紙で挟んだ薄い綴じ本を見つけたことがあるんだけど、見ただけで何だか寒気がして。もう触るなんてとんでもなくて、さっさと蔵から出ちゃったのさ"),
            who.do("その本の存在を忘れていた訳じゃないんだろうけど、その時はたまたまお客さんが多くて、つい朋久君に自分で蔵に入って好きな本を持ってってくれって、言ってしまったんだ"),
            who.do("祖父さんが何とか客を捌いた後で蔵に入ってみると、朋久君が手に持っててね"),
            who.do("小さな手が、黒い背表紙の薄い綴じ本を、持ってて"),
            who.do("最初はそれが何なのか、祖父さんも分からなかったんだって"),
            who.do("その時の朋久君の目が、初めて笑ってたそうなんだ。そっちの方がずっと印象的で、その本はよっぽど美味しかったんだろうなって思っただけだったんだってさ"),
            who.do("ただいつもならその場で全部のページを食べてしまうのに、何故かその日だけは本を持って帰ったそうなんだ。表紙だけ残ってたのか、それとも食べなかったのか、今もそれは分からないんだけど、私なんかは食べちゃったんじゃないかなって思ってる"),
            who.do("その次の日にね、彼は店に来なかった"),
            who.do("次の日も、もっと先の日も、ずっと彼は店に来なくなった"),
            who.do("引っ越したりした訳じゃないんだ。周りに聞いても誰も朋久なんて子のことを知らなくてね"),
            who.do("祖父さんは遂に朋久が家に閉じ込められてしまったんだ、って言ってた。当時は外に出さない、見せないようにしている、そういう類の子も結構いたらしいから。話を聞かされた時には、ああそうなんだ、って思ったよ"),
            who.do("ただね、朋久君が消えた日から、ちょくちょく蔵の本が消えるようになったんだ。殆ど見に行かないものだから、最初に気づいたのは一月くらいしてかららしいけど、本がね、あの子が消えた日の半分程度まで減ってたそうなんだよ"),
            who.do("祖父さんは誰かが盗んでいるんだって思ったそうなんだが、蔵には鍵も掛けてあったし、誰も入れないはずなんだよ。それなのに、本はどんどん減っていって、一年ほどで全て消えてしまったんだ"),
            w.symbol("　　　　※"),
            who.talk("その話を聞いてから、一度蔵に入ったことがあってね。見上げるほど積んであった本が、一冊も無くなってた。ただ、何だろうね。床に一枚だけ、紙の切れ端が落ちてたんだ。千切ったというより、誰か噛《か》んだような、そんな形でね"),
            who.do("あなたの湯呑みはすっかり冷めてしまっていたが、まだ一滴として中の液体は飲まれていなかった"),
            who.talk("昔はね、間引きって言って、色々と問題がある子なんかは、その、間引かれていなくなったんだよ"),
            who.do("老婆はやっとその眼鏡の目をあなたに向ける。右の方は白濁して、よく見えていないのだろうと感じた。ただ、思ったほどには皺《しわ》がなく、見た目よりずっと若いのかも知れない"),
            who.talk("万引きの語源が、間引きだっていう話は、知ってるかい？"),
            who.do("そう言うと、店主はあなたの盗った本を持ち上げ、ゆっくりと首を横に振った"),
            )

def sc_vanish_book(w: World):
    who = w.get("who")
    return w.scene("本が消える音",
            who.talk("もう二度とするんじゃないよ"),
            who.do("そう言われ、あなたは今、自分が棚から抜いた本を手に、店の裏手のドアを出た。その本はもう返本するから裏の蔵にある返本用の段ボール箱に入れてきてくれないか、と頼まれたからだ"),
            who.do("既に雨は上がっていたが、地面は生え散らかした雑草が水分を含み、歩を進める度にじゅわりと広がる。左手の方に蔦《つた》に覆われた白かったであろう壁があり、屋根の瓦は何枚か剥がれ落ちていた。それが地面に破片となっていたが、入り口の前だけは綺麗に取り除いてあった"),
            who.do("蔵の観音開きになった戸を、本を持ち替えて、右手で引っ張る。中から誰かが押さえているのかと思うほどの抵抗があったが、それが不意に摩擦音を上げて開いた"),
            who.do("ふっと、臭う。黴臭いが、それだけではない。もっと複雑な清濁入り交ざったものだ"),
            who.do("中に入ったあなたは手探りで壁に明かりのスイッチがないかと思うが、何も触れなかった。まだ夜まで時間があるものの外は明るいとは言えない。太陽の欠片でも見えればそうでもないだろうが、とても望める状況ではない"),
            who.do("仕方ない、と諦め、店主に言われた返本用の段ボール箱を探す"),
            who.do("しかし、蔵の中にはそんなもの、一つもない"),
            who.do("生温かい風が、頬《ほお》を撫《な》でていった"),
            who.do("何だろう"),
            who.do("蔵の奥を見る"),
            who.do("そこに、一枚の紙切れがあった。端が千切れているものだ"),
            who.do("さっきあったろうか"),
            who.do("自問しながら確かめようと一歩を踏み出した"),
            who.do("その足音がしたのだと、あなたは思った"),
            who.do("だが立ち止まっても、音は続いている"),
            who.do("しゃ、しゃ、という摩擦音。くしゃり、という何か軽いものを潰す音。それが鼓膜を通じて、あなたに響いている"),
            who.do("しゃしゃ、くしゃ"),
            who.do("しゃしゃ、くしゃり"),
            who.do("右か。いや左か"),
            who.do("あなたは振り返り、蔵の入り口を見た。外が薄ぼんやりと見える"),
            who.do("手にした本を、あなたは一度だけ見て、その足元に投げようとした、"),
            who.do("その手だった"),
            who.do("別の体温が、触れた"),
            who.do("思わず本を落としてしまう"),
            who.do("けれどその本は床にまで届かずに、すうっと消えてしまった"),
            who.do("喉を、あなたの唾液が通る"),
            who.do("小さく膝が震えた"),
            who.do("慌てて振り返り、体をここから出そうとする"),
            who.do("でも動かない"),
            who.do("いや、動けない"),
            who.do("入り口は見えているのに、体の前に、何かがいる"),
            who.do("ほう、とやや甘い、苺のそれにも似た芳香が漂った"),
            who.do("べり、と紙を割く音が、蔵に響く"),
            who.do("背後を見る"),
            who.do("何もいない"),
            who.do("居るはずがない"),
            who.do("その目の前を、一枚の本のページが舞った。一瞬確認できた文章は、あなたが数日までまで読み耽っていた本のそれだと、理解してしまった"),
            who.do("あなたの本は、消えていなかったのだ"),
            who.do("そう思ったあなたの右の頬が、あなた以外の手で触れられた"),
            who.do("心臓は信じられない速度で動き、息が止まる"),
            who.do("鼻腔を苺の匂いが満たした"),
            who.do("分からない"),
            who.do("両目を涙が覆った"),
            who.do("声は出ない"),
            who.do("たすけて"),
            who.do("という言葉が、消える"),
            who.do("あなたの耳に、何かを喰む音だけが響いてくる"),
            who.do("それは徐々に近くなり、やがて、あなたの右の耳たぶに、液体が触れた"),
            w.symbol("　　　　※"),
            who.do("鳳書店の店主は、結局飲まれることはなかった客用のお茶を、すっかり冷たくなっていたけれど、喉を鳴らして飲み干した"),
            who.do("いつからだろう"),
            who.do("いや、知っていた"),
            who.do("ただ、黙っていただけだ"),
            who.do("小さな震動があり、蔵の戸が閉められたのだと分かった"),
            who.do("店主は裏手を見やり、口の中で、声を掠《かす》らせた"),
            who.talk("朋久君……"),
            who.do("だがそれに答える人間《・・》は、もうそこにいなかった"),
            )


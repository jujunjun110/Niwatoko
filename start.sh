# 辞書ファイルを更新 
iconv -f utf8 -t eucjp ./settings/orders.yomi | ./vendor/julius-4.3.1/gramtools/yomi2voca/yomi2voca.pl > ./orders/orders.dic

# assign mic 
export ALSADEV="plughw:0,0"


file=./vendor/julius-4.3.1/julius/julius
if [ -e $file ];
then
	# linux environment
	./vendor/julius-4.3.1/julius/julius -C ./orders/orders.jconf -charconv EUC-JP UTF-8 -module &
else
	# macintosh environment
	./vendor/julius-4.3.1/julius/julius.dSYM -C ./orders/orders.jconf -charconv EUC-JP UTF-8 -module &
fi

sleep 2
python -B niwatoko_controller.py

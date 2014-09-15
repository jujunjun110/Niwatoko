# 毎回辞書ファイルを更新 
iconv -f utf8 -t eucjp ./orders/orders.yomi | ./vendor/julius-4.3.1/gramtools/yomi2voca/yomi2voca.pl > ./orders/orders.dic


file=./vendor/julius-4.3.1/julius/julius
if [ -e $file ];
then
	# linux environment
	./vendor/julius-4.3.1/julius/julius -C ./orders/orders.jconf -charconv EUC-JP UTF-8 -module &
else
	# macintosh environment
	./vendor/julius-4.3.1/julius/julius.dSYM -C ./orders/orders.jconf -charconv EUC-JP UTF-8 -module &
fi

sleep 5
python -B niwatoko_controller.py

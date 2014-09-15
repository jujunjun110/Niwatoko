file="./vendor/julius-4.3.1/julius/julius"
if [-f file]
then
	# linux environment
	./vendor/julius-4.3.1/julius/julius -C ./orders/orders.jconf -charconv EUC-JP UTF-8 -module &
else
	# macintosh environment
	./vendor/julius-4.3.1/julius/julius.dSYM -C ./orders/orders.jconf -charconv EUC-JP UTF-8 -module &
fi
sleep 5
python niwatoko_controller.py

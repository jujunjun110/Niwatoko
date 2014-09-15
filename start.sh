./vendor/julius-4.3.1/julius/julius -C ./orders/orders.jconf -charconv EUC-JP UTF-8 -module &
sleep 5
python niwatoko_controller.py

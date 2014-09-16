Niwatoko
========

Enable you to manipulate electronics with your voice as if "Niwatoko cane" in Harry Potter


## 事前準備
- Raspberry Pi + Raspbian で動作を確認
- USBマイク, IRKit, インターネット接続必須
- PyYAMLモジュールをインストールしておく必要あり
- マイクの設定はここの通りにやるとうまくいく（http://cubic9.com/Devel/%C5%C5%BB%D2%B9%A9%BA%EE/RaspberryPi/%C6%FC%CB%DC%B8%EC%B2%BB%C0%BC%C7%A7%BC%B1/）

## 使い方
1. vendor ディレクトリでsetup.shを実行（Juliusがvendorディレクトリによしなにインストールされます）
2. myhome_conf.yaml.sampleをもとにmyhome_conf.yamlを作成し、自分のIRKitのローカルIPと、認識させたい言葉、IRKitのデータを書く
3. start.shを実行（5秒くらいで音声受付の準備が整う）

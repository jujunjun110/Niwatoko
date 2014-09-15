wget --trust-server-names 'http://sourceforge.jp/frs/redir.php?m=jaist&f=%2Fjulius%2F60273%2Fjulius-4.3.1.tar.gz'
wget --trust-server-names 'http://sourceforge.jp/frs/redir.php?m=jaist&f=%2Fjulius%2F59050%2Fdictation-kit-v4.2.3.tar.gz'
wget --trust-server-names 'http://sourceforge.jp/frs/redir.php?m=jaist&f=%2Fjulius%2F51159%2Fgrammar-kit-v4.1.tar.gz'

# ライブラリの展開
tar xvzf julius-4.3.1.tar.gz
tar xvzf dictation-kit-v4.2.3.tar.gz
tar xvzf grammar-kit-v4.1.tar.gz

# インストーラーの削除
rm *.tar.gz

# juliusのインストール
cd julius-4.3.1
./configure
make
make install




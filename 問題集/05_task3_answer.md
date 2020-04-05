[< 目次へ戻る](README.md#目次)

# 答え合わせ


## 問1

```shell
mkdir Shirataki/
mkdir Shirataki/Inaba/
mkdir Shirataki/Inaba/Kenmotsu/
mkdir Shirataki/Inaba/Kenmotsu/Sato/
mkdir Shirataki/Inaba/Kenmotsu/Sato/Daigo/
mkdir Shirataki/Inaba/Kenmotsu/Sato/Etsuma/
mkdir Shirataki/Inaba/Kenmotsu/Usui/
mkdir Shirataki/Inaba/Kenmotsu/Usui/Watanabe/
mkdir Shirataki/Inaba/Kenmotsu/Usui/Kamijou/
mkdir Shirataki/Inaba/Kenmotsu/Usui/Oobuchi/
mkdir Shirataki/Inaba/Kenmotsu/Fukaishi/
mkdir Shirataki/Inaba/Kenmotsu/Fukaishi/Goto/
mkdir Shirataki/Inaba/Kenmotsu/Fukaishi/Kondo/
mkdir Shirataki/Inaba/Kenmotsu/Nishimura/
mkdir Shirataki/Inaba/Kenmotsu/Nishimura/Yamamoto/
mkdir Shirataki/Inaba/Kenmotsu/Hatano/
mkdir Shirataki/Inaba/Kenmotsu/Hatano/Yabe/
mkdir Shirataki/Inaba/Kenmotsu/Hatano/Andou/
```


## 問2
　`chmod`コマンドで使うパーミッションの記述で、  
8進数の`740`の意味を説明してみましょう。  

> ****  

**正解** です。  

同一ユーザからは読み書き・実行すべてが可能で、同一グループのユーザからは読み取り専用となります。  
グループが異なるユーザからは読み取りも許されません。  


## 問3
　`umask`の意味を説明してみましょう。  

> ****  

**正解** です。  

ファイルのデフォルトのアクセス権は「0666 - umask」となり、  
ディレクトリは「0777 - umask」となります。  


## 問4
　シェル変数と環境変数の違いは何ですか？  

> ****  

**正解** です。  

シェル変数はそのシェル内でのみ有効な変数で、環境変数はシェルが終了した後も有効な変数です。  


## 問5
　`while`文と`until`文の違いは何ですか？  

> ****  

**正解** です。  

`while`文は条件を **満たすあいだ** 処理を繰返し、`until`文は条件を **満たすまで** 処理を繰り返します。  


## 問6
　シェルスクリプトにおける、以下の2つの違いは何ですか？  

```shell
if [ $val == '20' ]
if [ $val -eq 20  ]
```

> ****  

**正解** です。  

前者は変数`val`が文字列の`'20'`かどうか判定しており、  
後者は数値の`20`と等しいかどうかを判定しています。  



## 問7
　`20`以上の値を入れると「`you can drink.`」と出力されるスクリプトを作製してください。  

```shell
read age

if [ $age -ge 20 ]
then
        echo 'you can drink.'
fi
```

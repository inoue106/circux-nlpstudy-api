circux-nlpstudy-api
====

このソースコードは自然言語処理の検討用に作成したAPIです。

## Description
社内の専門家検索システムの構築をする上で、職務経歴書などの文章から効率的に検索する手法が課題になっており、かねてから注目している機械学習処理系の調査を進めている。機械学習界隈では特にPythonによる実装が目立っており、2020年冬現在では、ginzaという自然言語処理ライブラリが注目されているようだ。また、HR業界でも、株式会社ビズリーチが「HR領域のワードベクトル」を提供していたり、各社機械学習によるs様々なアプローチを検討しているようである。そこで、AWSなどのクラウド環境で環境を構築しやすいよう、Dockerでの最低限の環境と、軽量Webフレームワークを構築した。

### 使用したライブラリ
* nlp関連
    * [ginza](https://megagonlabs.github.io/ginza/)
    * [gensim](https://radimrehurek.com/gensim/) (word2vec)
    * [HR領域の単語ベクトル](https://github.com/bizreach/ai/tree/master/word2vec)
* Webフレームワーク
    * [Flask](https://flask.palletsprojects.com/)


## Demo

## VS. 

## Requirement
* docker / docker-compose

## Usage

## Install
`docker-compose.yml`のあるディレクトリで、下記を実行。初回は叩いてからAPIにアクセスできるようになるまでに1時間弱かかる。
```
docker-compose up --build
```

## Contribution

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[inoue106](https://github.com/inoue106)

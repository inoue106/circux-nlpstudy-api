circux-nlpstudy-api
====

このソースコードは自然言語処理の検討用に作成したAPIです。

## Description
社内の専門家検索システムの構築をする上で、職務経歴書などの文章から効率的に検索する手法が課題になっており、かねてから注目している機械学習処理系の調査を進めている。機械学習界隈では特にPythonによる実装が目立っており、MecabやJanomeを使った仕組みがweb上では良く見つかり情報も多いが、環境を構築するのはちょっと面倒くさい。尚、2020年冬現在では、ginzaという自然言語処理ライブラリが注目されているようだ。また、HR業界でも、株式会社ビズリーチが「HR領域のワードベクトル」を提供していたり、各社機械学習による様々なアプローチを検討しているようである。そこで、弊社でも、機械学習系の活用が推進できるように、Dockerでの最低限の環境と、軽量Webフレームワークを構築した。

### 使用したライブラリ
* nlp関連
    * [ginza](https://megagonlabs.github.io/ginza/)
    * [gensim](https://radimrehurek.com/gensim/) (word2vec)
    * [HR領域の単語ベクトル](https://github.com/bizreach/ai/tree/master/word2vec)
* Webフレームワーク
    * [Flask](https://flask.palletsprojects.com/)

### ディレクトリ構成
* root
    * docker-compose.yml - 統合環境構築用定義
    * docker
        * python
            * Dockerfile - Python環境を構築するDockerfile
    * models - gensimの学習済モデルを配置するディレクトリ
    * src
        * static - jsやcss
        * templates - HTMLテンプレート
        * server.py - docker-composeで起動されるスクリプト

### 簡単な設計思想
* 初回ビルドでgensimとginza、flaskの最低限の環境を構築する
* server.py にルーティングとサービス起動が記述されているので、これを読めば全部わかる
    * 最初のrootブロックが初期化、全体で共有するオブジェクトもここで定義
    * @app.routeブロックがルーティングの定義
        * 基本的にはPOSTで受けJSONで返す
    * 最後の if __name__ == "__main__": ブロックがサーバの定義

## Demo

## VS. 

## Requirement
* docker / docker-compose

## Usage

## Install
* modelsの下に「HR領域の単語ベクトル」より取得したbinを配置する。
* `docker-compose.yml`のあるディレクトリで、下記を実行する。
    * 初回は叩いてからAPIにアクセスできるようになるまでに1時間弱かかる。
```
docker-compose up --build
```

## Contribution

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[inoue106](https://github.com/inoue106)

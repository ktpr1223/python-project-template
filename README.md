# python-project-template
python用のプロジェクトテンプレート

## How to use
### Requirements

``` shell
pip install cookiecutter
```

### Usage

プロジェクト開始

``` shell
cookiecutter https://github.com/ktpr1223/python-project-template
```

インストール

``` shell
# install
make install

# develop
make develop

# uninstall
make uninstall
```

テスト

``` shell
# test
make test

# test-coverage
make test-coverage
```

lint

``` shell
make lint
```

## folder構成
```
├── Makefile           <- Makefile よく使うコマンドなど
│
├── README.md          <- README
│
├── setup.py           <- src以下をinstallする
│
├── requirements.txt   <- pythonなので
│
├── {{cookiecutter.project_name}} <- ライブラリ
│
├── tests              <- srcに関するテスト
│
└── tox.ini            <- tox file
```

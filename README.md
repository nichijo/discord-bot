# これなに
DiscordでVoiceChatに入室・退出したら任意のチャンネルに発言するBot

## どうやって使う？

1. `python3`をインストールしましょう。
2. `pip install -r requirements.txt`  
3. `.env`ファイルを`.env_default`を元に作る（tokenとチャンネルIDはよしなに）  
4. `python ./bot.py`
実行する。

## dockerの場合

Dockerの場合は、`.env`ファイル作り `--env-file .env` とするか
```
docker build -t tag .
docker run --rm --env-file .env
```

環境変数を `--env` で渡すようにしてください。
```
docker run --rm --env TOKEN=your_token
```
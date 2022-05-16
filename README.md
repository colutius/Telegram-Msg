# Telegram-Msg

通过actions向telegram发送消息

[![test](https://github.com/colutius/Telegram-Msg/actions/workflows/main.yml/badge.svg)](https://github.com/colutius/Telegram-Msg/actions/workflows/main.yml)

## 开始使用

发送一条自定义消息

```yml
name: Telegram-Msg
on: [push]
jobs:
  sendMsg:
    name: sendMsg
    runs-on: ubuntu-latest
    steps:
    - uses: colutius/Telegram-Msg@main
      with:
        token: ${{ secrets.TELEGRAM_TOKEN }}
        chatid: ${{ secrets.TELEGRAM_TO }}
        message: |
          👇新的提交👇
          
          👤提交人: [${{ github.actor }}]

          📄提交信息: ${{ github.event.commits[0].message }}

          📦仓库: ${{ github.repository }}
        button: true
        button_name: 👀查看更改👀
        button_url: https://github.com/${{ github.repository }}/commit/${{github.sha}}
```

不加可选参数发送默认消息

```yml
- uses: colutius/Telegram-Msg@main
  with:
    token: ${{ secrets.TELEGRAM_TOKEN }}
    chatid: ${{ secrets.TELEGRAM_TO }}
```

## 可选参数

* button: `true`或`false`，是否添加链接按钮，默认为`true`
* button_name: 按钮名称，默认为👀查看更改👀
* button_url: 按钮链接地址，默认为`https://github.com/${{ github.repository }}/commit/${{github.sha}}`


## Secrets

* `token`:  Telegram bot token
* `chatid`: chat id

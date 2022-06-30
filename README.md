# Telegram-Msg

通过actions向telegram发送消息

[![test](https://github.com/colutius/Telegram-Msg/actions/workflows/main.yml/badge.svg)](https://github.com/colutius/Telegram-Msg/actions/workflows/main.yml)

## 开始使用
> 注意，请始终使用最新版本
> 如`- uses: colutius/Telegram-Msg@main`或`- uses: colutius/Telegram-Msg@latest`，由于在dockerhub只保存了最新的镜像，所以无论你使用哪个版本，实际都是使用最新的镜像，为了避免出现各种奇怪的问题，请避免使用旧版本

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
        is_notify: true
        is_preview: true
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
* button_name: 按钮名称，默认为`👀查看更改👀`
* button_url: 按钮链接地址，默认为`https://github.com/${{ github.repository }}/commit/${{github.sha}}`
* is_notify: `true`或`false`，是否消息提醒，若为否，则发送没有声音的通知，默认为`true`
* is_preview: `true`或`false`，是否预览链接，默认为`true`


## Secrets

* `token`:  Telegram bot token
* `chatid`: chat id

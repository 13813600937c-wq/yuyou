name: 钉钉每日提醒（加签版）
on:
  schedule:
    - cron: '0 1 * * *'
  workflow_dispatch:

jobs:
  ding-remind:
    runs-on: ubuntu-latest
    steps:
      - name: 拉取代码
        uses: actions/checkout@v4

      - name: 配置Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: 安装依赖
        run: pip install requests

      - name: 执行钉钉提醒脚本
        env:
          DING_WEBHOOK: ${{ secrets.DING_WEBHOOK }}
          DING_SECRET: ${{ secrets.DING_SECRET }}
        run: python ding_remind.py

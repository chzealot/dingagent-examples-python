#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import asyncio
import dingtalk_stream


class HelloHandler(dingtalk_stream.GraphHandler):
    async def process(self, callback: dingtalk_stream.CallbackMessage):
        request = dingtalk_stream.GraphRequest.from_dict(callback.data)
        body = json.loads(request.body)
        await self.reply_markdown(body['sessionWebhook'], '- 天气：晴\n- temperature: 22')
        return dingtalk_stream.AckMessage.STATUS_OK, self.get_success_response({'success': True}).to_dict()

async def hello():
    credential = dingtalk_stream.Credential(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))
    client = dingtalk_stream.DingTalkStreamClient(credential)
    client.register_callback_handler(dingtalk_stream.graph.GraphMessage.TOPIC, HelloHandler())
    await client.start()

if __name__ == '__main__':
    asyncio.run(hello())
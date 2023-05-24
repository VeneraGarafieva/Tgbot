from core.base import Service
from core.domains import Webhook as WebhookDomain


class Webhook(Service):
    def set(self, webhook: WebhookDomain) -> WebhookDomain | None:
        self.http.request('/setWebhook', data={
            'url': webhook.url
        })
        return self.get()

    def delete(self) -> WebhookDomain | None:
        self.http.request('/deleteWebhook')
        return self.get()

    def get(self) -> WebhookDomain | None:
        query = self.http.request('/getWebhookInfo')
        if not query.status or not query.data:
            return
        return WebhookDomain(
            url=query.data.get('url'),
            has_certificate=query.data.get('has_custom_certificate', False)
        )


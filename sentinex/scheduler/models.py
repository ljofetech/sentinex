from django.db import models


class Endpoint(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    check_interval = models.IntegerField(default=5)  # в минутах
    last_checked = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    notify_on_failure = models.BooleanField(default=True)

    def __str__(self):
        return f"""
            Name: {self.name},
            URL: {self.url}
        """


class CheckLog(models.Model):
    endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)
    status_code = models.IntegerField()
    response_time = models.FloatField()
    is_up = models.BooleanField()
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"""
            Endpoint: {self.endpoint},
            Status_code: {self.status_code}
        """

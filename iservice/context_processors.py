from django.utils import timezone
from datetime import timedelta
from .models import Task  # adjust import as needed

def notifications_processor(request):
    if request.user.is_authenticated:
        today = timezone.now().date()
        end_date = today + timedelta(days=5)

        notifications = Task.objects.filter(
            user=request.user,
            deadline__range=[today, end_date]
        ).exclude(role='Done')
        return {'notifications': notifications}
    return {}

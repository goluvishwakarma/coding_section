# Date: 13-01-2021, author: golu

# python -m pip install win10toast
from win10toast import ToastNotifier

# one-time initialization
toaster = ToastNotifier()

# show notification whenever needed
toaster.show_toast("Notification", "Alert! Yes", threaded=True, icon_path=None, duration=3)  # 3 seconds

# to check if any notification are active,
# use 'toaster.notification_active()'
import time

while toaster.notification_active():
    time.sleep(0.1)

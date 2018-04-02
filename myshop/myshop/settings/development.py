from .base import *
from django.urls import reverse_lazy

DEBUG = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
PAYSTACK_PUBLIC_KEY = 'pk_test_ce5845c17769524b94ea90ba7ad352d8f3c9d7f1'
PAYSTACK_SECRET_KEY = 'sk_test_3bd9afd1854eb8f592a8b5d1de6982085683f500'
PAYSTACK_FAILED_URL = reverse_lazy('payments:canceled')
PAYSTACK_SUCCESS_URL = reverse_lazy('payments:done')
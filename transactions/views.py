from django.conf import settings
from django.core.exceptions import ValidationError
from transactions.models import Transaction
from django.http import JsonResponse
import os
import csv

# Create your views here.
def initialise(request):
    try:
        csv_file_path = os.path.join(settings.BASE_DIR, 'public\static\\transactions_data_backend__1_.csv') 
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Transaction.objects.create(
                    user=row['user'],
                    date=row['date'],
                    type=row['transaction_type'],
                    amount=row['amount'],
                )
        return JsonResponse({'status': 'Transactions imported successfully', 'code': 200})
    except FileNotFoundError:
        return JsonResponse({'status': 'CSV file not found', 'code': 404})
    except ValidationError as e:
        return JsonResponse({'status': str(e), 'code': 400})

    

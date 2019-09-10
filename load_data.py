import json
import django

django.setup()

from mealdeal.md.models import Item

data = {}
with open("data.json", "r") as f:
    data = json.loads(f.read())

for v in data.values():
    Item.objects.create(**v)

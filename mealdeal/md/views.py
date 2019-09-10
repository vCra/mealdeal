from pprint import pprint

from django.views.generic import TemplateView

from .models import Item


class HomeView(TemplateView):
    template_name = "md/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        items = {
            "main_item": Item.objects.filter(category__name="main").order_by('?').first(),
            "snack_item": Item.objects.filter(category__name="snack").order_by('?').first(),
            "drink_item": Item.objects.filter(category__name="drink").order_by('?').first(),
        }
        total_price = sum(map(lambda x: x.price, items.values()))
        items.update({
            "total_price": total_price,
            "savings": total_price - 3
        })
        context.update(items)
        return context

class MaxCostView(TemplateView):
    template_name = "md/max_cost.html"

    def get_context_data(self, **kwargs):
        context = super(MaxCostView, self).get_context_data()
        items = {
            "main_items": Item.objects.filter(category__name="main", price=Item.objects.filter(category__name="main").order_by("price").last().price),
            "snack_items": Item.objects.filter(category__name="snack", price=Item.objects.filter(category__name="snack").order_by("price").last().price),
            "drink_items": Item.objects.filter(category__name="drink", price=Item.objects.filter(category__name="drink").order_by("price").last().price),
        }
        context.update(items)
        return context




class MinCostView(TemplateView):
    template_name = "md/max_cost.html"

    def get_context_data(self, **kwargs):
        context = super(MinCostView, self).get_context_data()
        items = {
            "main_items": Item.objects.filter(category__name="main", price=Item.objects.filter(category__name="main").order_by("price").first().price),
            "snack_items": Item.objects.filter(category__name="snack", price=Item.objects.filter(category__name="snack").order_by("price").first().price),
            "drink_items": Item.objects.filter(category__name="drink", price=Item.objects.filter(category__name="drink").order_by("price").first().price),
        }
        context.update(items)
        return context

class AllCostView(TemplateView):
    template_name = "md/max_cost.html"

    def get_context_data(self, **kwargs):
        context = super(AllCostView, self).get_context_data()
        items = {
            "main_items": Item.objects.filter(category__name="main"),
            "snack_items": Item.objects.filter(category__name="snack"),
            "drink_items": Item.objects.filter(category__name="drink"),
        }
        context.update(items)
        return context

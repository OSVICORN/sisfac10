import csv
from django.core.management import BaseCommand
from django.utils import timezone

from inv.models import Categoria, SubCategoria, Producto


class Command(BaseCommand):
    help = "Loads products and product categories from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        start_time = timezone.now()
        file_path = options["file_path"]
        with open(file_path, "r") as csv_file:
            data = csv.reader(csv_file, delimiter=",")
            product_categories = {p_category.code: p_category for p_category in Categoria.objects.all()}
            products = []
            for row in data:
                product_category_code = row[4]
                product_category = product_categories.get(product_category_code)
                if not product_category:
                    product_category = Categoria.objects.create(name=row[3], code=row[4])
                    product_categories[product_category.code] = product_category
                product = Producto(
                    name=row[0],
                    code=row[1],
                    price=row[2],
                    product_category=product_category
                )
                products.append(product)
                if len(products) > 5000:
                    Producto.objects.bulk_create(products)
                    products = []
            if products:
                Producto.objects.bulk_create(products)
        end_time = timezone.now()
        self.stdout.write(
            self.style.SUCCESS(
                f"Loading CSV took: {(end_time-start_time).total_seconds()} seconds."
            )
        )
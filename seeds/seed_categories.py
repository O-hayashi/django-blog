from blogs.models import Category

categories = [
    "Technology",
    "Web Development",
    "Programming",
    "Artificial Intelligence",
    "Cybersecurity",
    "Data Science",
    "Career & Learning"
]

for category in categories:
  Category.objects.get_or_create(category_name = category)

print("Categories created successfully")

# python manage.py shell < seed_categories.py
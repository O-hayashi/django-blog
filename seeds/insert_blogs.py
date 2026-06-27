from django.contrib.auth.models import User
from django.utils.text import slugify
from blogs.models import Category, Blog
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()
user = User.objects.first()

category, _ = Category.objects.get_or_create(
    category_name="Technology"
)

featured_blogs = [
    {
        "title": "The Rise of Artificial Intelligence in Everyday Life",
        "desc": "Explore how AI is transforming industries, education, healthcare, and our daily routines.",
        "body": """Artificial Intelligence has moved beyond science fiction and become an integral part of modern life. From virtual assistants to recommendation systems, AI powers many services we use daily.

Businesses are adopting AI to automate repetitive tasks, improve customer experiences, and make data-driven decisions. As technology advances, understanding AI becomes increasingly important for students and professionals alike."""
    },
    {
        "title": "10 Essential Programming Skills Every Student Should Learn",
        "desc": "A guide to the most valuable programming skills for aspiring software developers.",
        "body": """Programming is more than writing code. Developers must understand problem-solving, debugging, version control, databases, and software design.

Students who master these skills early gain a significant advantage when applying for internships and jobs in the technology sector."""
    },
    {
        "title": "Why Cybersecurity Matters More Than Ever",
        "desc": "Learn why protecting digital information has become a top priority in the modern world.",
        "body": """Cyber threats continue to grow as businesses and individuals rely more on digital systems.

Understanding cybersecurity fundamentals such as strong passwords, encryption, and network security can help reduce risks and protect sensitive information."""
    }
]

for blog in featured_blogs:
    Blog.objects.create(
        title=blog["title"],
        slug=slugify(blog["title"]),
        category=category,
        author=user,
        featured_image="uploads/default.jpg",
        short_description=blog["desc"],
        blog_body=blog["body"],
        status="Published",
        is_featured=True
    )

normal_blogs = [
    {
        "title": "Getting Started with Django Web Development",
        "desc": "A beginner-friendly introduction to building websites using Django.",
        "body": "Django is a powerful Python framework that helps developers build secure and scalable web applications quickly."
    },
    {
        "title": "Understanding REST APIs for Beginners",
        "desc": "Learn how applications communicate using REST APIs.",
        "body": "REST APIs allow software systems to exchange data over the internet using standard HTTP methods."
    },
    {
        "title": "How Git and GitHub Improve Team Collaboration",
        "desc": "Version control made simple for students and professionals.",
        "body": "Git helps track code changes while GitHub provides a platform for collaboration and project management."
    },
    {
        "title": "Top 5 Database Concepts Every Developer Must Know",
        "desc": "Master the fundamentals of working with databases.",
        "body": "Understanding tables, relationships, indexes, normalization, and queries is essential for every developer."
    },
    {
        "title": "The Future of Cloud Computing",
        "desc": "Discover how cloud technologies are shaping modern software.",
        "body": "Cloud computing enables organizations to deploy applications faster and scale infrastructure efficiently."
    },
    {
        "title": "A Beginner's Guide to Object-Oriented Programming",
        "desc": "Understand the core concepts of OOP with simple examples.",
        "body": "Classes, objects, inheritance, polymorphism, and encapsulation form the foundation of OOP."
    },
    {
        "title": "How Students Can Build a Strong Developer Portfolio",
        "desc": "Practical tips for showcasing your projects and skills.",
        "body": "A strong portfolio demonstrates technical skills, problem-solving ability, and consistency in learning."
    }
]

for blog in normal_blogs:
    Blog.objects.create(
        title=blog["title"],
        slug=slugify(blog["title"]),
        category=category,
        author=user,
        featured_image="uploads/default.jpg",
        short_description=blog["desc"],
        blog_body=blog["body"],
        status="Published",
        is_featured=False
    )